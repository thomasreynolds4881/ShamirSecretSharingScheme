# ShamirSecretSharingScheme
Generates and decodes strings to be used with Shamir's Secret Sharing Scheme.

## How it works
By splitting a password into segments that can only be solved once all/some of the pieces are put together, it guarantees that a password is kept secret. A more in-depth explaination of the method is given on Wikipedia: https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

## How to use it
Use CreatePass.py to create a password that will be split as many times as you'd like (at a max of the length of the string) and then use DecodePass.py to decode a complete list of these strings. If the list is incomplete, it will give a best guess.

## Goals
- Implement full SSS using a slope and points to encrypt.
- Allow an overlapping option so that three parts might be generated, but you only need two parts to solve the password.

## Files
- CreatePass.py: takes a string and converts it into a list of split strings that are written to a file
- DecodePass.py: combines a list of strings in an attempt to decipher them

## Notes
I had the idea to make this from the YouTube channel standupmaths: https://www.youtube.com/watch?v=K54ildEW9-Q
