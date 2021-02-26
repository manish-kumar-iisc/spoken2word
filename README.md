# Spoken 2 Written

This Python module can convert a paragraph of spoken English to written English.

 For example, "two dollars" would be converted to '$2'. Abbreviations spoken as "C M" or "Triple A" would be written as "CM" and "AAA" respectively.


## Installation: 
  You can install the module using Python Package Index using the below command.
   ```
   >> python3 setup.py install
   ```

## Usage:

**Successful Example:**
   ```
    >>python3
	>>from spoken2written import spkn2wrtn
	>>sp2wr.convert_spkn_2_wrtn()
	>>
	[IN]:Enter Your paragraph of spoken english:
	
	My name is Manish. I wake up before 6 A M. I go to sleep before 10 P M. I got hundred dollars today. My mobile number is double 9, quadruple 8, single 1 and triple 3. 
	
	[OUT]:The input Spoken English Paragraph: 
	
	"My name is Manish. I wake up before 6 A M. I go to sleep before 10 P M. I got hundred dollars today. My mobile number is double 9, quadruple 8, single 1 and triple 3."
		
	 Converted Written English Paragraph: 
	 
	 "My name is Manish. I wake up before 6 AM. I go to sleep before 10 PM. I got $100 today. My mobile number is 99, 8888, 1 and 333."
```

## Note: 

   **The above code may fail due to some formatting issues in the text. Also the package might give incorrect example for rules that we has not been defined in the rules set. User may wish to add them before installtion step.**

## Here are some possible future functionalities that  can be covered in the future versions of the module:

1. Proper handling of punctuations.
2. Addition of more rules for conversion
