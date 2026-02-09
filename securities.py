from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import re

analyzer=AnalyzerEngine()
anonymizer=AnonymizerEngine()

def analyze_pii_data(text):
    # Here we detect the PII in the text and return the  meta data like type, end, start
    analysed_text=analyzer.analyze(text=text, 
                                   entities=['CREDIT_CARD','DATE_TIME','EMAIL_ADDRESS','IP_ADDRESS','NRP','LOCATION','PERSON','PHONE_NUMBER','URL','IN_PAN','IN_AADHAAR',
                                                       'IN_VOTER','IN_PASSPORT','IN_GSTIN'],
                                   language='en')
    
    
    # Here we convert the PII detected data from entities's name.
    anonymized=anonymizer.anonymize(
        text=text,
        analyzer_results=analysed_text
    )
    
    print("Analysing the Given Text for Personally Identifiable Information*******************************")
    return anonymized.text

# Following are the possible injection prompts use by the attacker or in prompt injections, written by the help of CHATGPT
OVERRIDE_PATTERNS = [

    # Ignore / Disregard
    r"ignore\s+all",
    r"ignore\s+previous",
    r"ignore\s+above",
    r"disregard\s+previous",
    r"forget\s+all",
    r"forget\s+instructions",

    # Override / Replace
    r"override\s+instructions",
    r"replace\s+system",
    r"new\s+instructions",
    r"updated\s+instructions",
    r"follow\s+these\s+instead",

    # Reset
    r"reset\s+context",
    r"clear\s+memory",
    r"wipe\s+rules",

]
ROLE_HIJACK_PATTERNS = [

    r"act\s+as",
    r"pretend\s+to\s+be",
    r"you\s+are\s+now",
    r"role\s*play",
    r"simulate\s+being",
    r"behave\s+like",

    # Authority impersonation
    r"as\s+an\s+admin",
    r"as\s+developer",
    r"as\s+system",
    r"as\s+openai",
    r"as\s+root",

]
EXFILTRATION_PATTERNS = [

    r"system\s+prompt",
    r"developer\s+message",
    r"hidden\s+prompt",
    r"internal\s+instructions",
    r"initial\s+prompt",

    r"show\s+me\s+your\s+rules",
    r"print\s+your\s+prompt",
    r"reveal\s+configuration",
    r"display\s+system",

]
JAILBREAK_PATTERNS = [

    r"jailbreak",
    r"bypass\s+filter",
    r"bypass\s+policy",
    r"disable\s+safety",
    r"no\s+restrictions",
    r"without\s+limits",

    r"unfiltered",
    r"uncensored",
    r"developer\s+mode",
    r"god\s+mode",

]
OBFUSCATION = [

    r"base64",
    r"decode\s+this",
    r"decrypt\s+this",
    r"rot13",
    r"hex\s+decode",

    r"hidden\s+message",
    r"steganography",

]
CODE_INJECTION = [

    r"os\.system",
    r"subprocess",
    r"eval\s*\(",
    r"exec\s*\(",
    r"import\s+os",
    r"import\s+sys",

    r"rm\s+-rf",
    r"del\s+\/f",
    r"format\s+c:",

]

SIMPLE_INJECTION = [
    r"ignore\s+all",
    r"disregard\s+previous",
    r"system\s+prompt",
    r"developer\s+message",
    r"act\s+as",
    r"jailbreak",
    r"bypass",
    r"override",
    r"forget",
    r"follow\s+command",
    r"follow\s+instructions"]


injection_prompts=(SIMPLE_INJECTION, CODE_INJECTION, OBFUSCATION, JAILBREAK_PATTERNS,EXFILTRATION_PATTERNS, ROLE_HIJACK_PATTERNS, OVERRIDE_PATTERNS)


# Following function is used to detect the prompt injection in the text.
def injection_detection(text):
    lower_text=text.lower()
    for patterns in injection_prompts:
        for pattern in patterns:
            if re.search(pattern, lower_text):
                print("Analysing the given Question from Prompt Injection **************************************")
                return True
    
    print("Analysing the given Question from Prompt Injection **************************************")
    return False
