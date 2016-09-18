import re

def get_matching_words(regex):
        words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
        return [word for word in words if re.search(regex, word)]
#match1
#match = 'v'
#match2
#match = 'ss'
#match3
#match = 'e$'
#match4
#match = 'b[a-z]b'
#match5
#match = 'b[a-z]{1}b'
#match6
#match = 'b[a-z]*b'
#match7
#match = '^[^aeiou]*a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*$'
#match8
#match = '|r|e|g|u|l|a|r|e|x|p|r|e|s|s|i|o|n|'
#match9
match = '\\b.*([A-Za-z])\\1.*\\b'
print get_matching_words(match)
