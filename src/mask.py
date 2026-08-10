import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessor, LogitsProcessorList

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

class AllowOnlyTokens(LogitsProcessor):
    def __init__(self, allowed_token_ids):
        self.allowed = torch.tensor(allowed_token_ids)

    def __call__(self, input_ids, scores):
        mask = torch.full_like(scores, float("-inf"))
        mask[:, self.allowed] = scores[:, self.allowed]
        return mask

# e.g. only allow digits
allowed_ids = [tokenizer.encode(c)[0] for c in "0123456789"]
input_ids = tokenizer("The result is ", return_tensors="pt").input_ids
output = model.generate(
    input_ids,
    max_new_tokens=10,
    logits_processor=LogitsProcessorList([AllowOnlyTokens(allowed_ids)]),
)
print(tokenizer.decode(output[0]))


import torch
import torch.nn.functional as F

input_ids = tokenizer("The second result is ", return_tensors="pt").input_ids

for _ in range(5):
    with torch.no_grad():
        logits = model(input_ids).logits[:, -1, :]   # logits for next token

    mask = torch.full_like(logits, float("-inf"))
    mask[:, allowed_ids] = logits[:, allowed_ids]     # manual masking step

    probs = F.softmax(mask, dim=-1)
    next_token = torch.argmax(probs, dim=-1, keepdim=True)  # or torch.multinomial for sampling
    input_ids = torch.cat([input_ids, next_token], dim=-1)

print(tokenizer.decode(input_ids[0]))


# https://huggingface.co/docs/transformers/internal/generation_utils

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# precompute the token ids allowed by our toy "grammar": digits + space
digit_token_ids = [
    tid for tok, tid in tokenizer.get_vocab().items()
    if tok.strip("Ġ").isdigit() or tok == "Ġ"
]

def grammar_fn(batch_id, input_ids):
    # batch_id: which sequence in the batch we're generating
    # input_ids: the tokens generated so far for this sequence
    # must return the list of token ids allowed as the NEXT token
    return digit_token_ids

input_ids = tokenizer("The password is", return_tensors="pt").input_ids

output = model.generate(
    input_ids,
    max_new_tokens=10,
    prefix_allowed_tokens_fn=grammar_fn,
)
print(tokenizer.decode(output[0]))


prompt_len = input_ids.shape[1]

def four_digit_grammar_fn(batch_id, input_ids):
    generated_so_far = input_ids[prompt_len:]  # tokens produced after the prompt
    if len(generated_so_far) >= 4:
        return [tokenizer.eos_token_id]         # force stop
    return digit_token_ids                       # otherwise, still only digits

output = model.generate(
    input_ids,
    max_new_tokens=10,
    prefix_allowed_tokens_fn=four_digit_grammar_fn,
)
print(tokenizer.decode(output[0]))

# This second version is a nice bridge to the "real" GCD libraries: grammar_fn here is a hand-written, hard-coded version of exactly what IncrementalGrammarConstraint computes automatically from an EBNF/GBNF grammar at every step — walk the automaton to the current state, return the set of tokens that keep you in the language. Good moment in a lecture to say "this is the function a CFG parser writes for you."

# One implementation detail worth flagging to students (a known open issue): if every token returned by prefix_allowed_tokens_fn happens to have a logit of -inf for some other reason, the constraint can silently fail to hold and the model may pick a token outside the allowed list — a good real-world caveat to pair with your Grammar-Aligned Decoding discussion about constrained decoding not always behaving exactly as advertised