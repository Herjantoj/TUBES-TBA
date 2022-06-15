import streamlit as st

st.title("Lexical Analyzer")
st.title("Kelompok 11 - Bahasa Spanyol")

col1, col2 = st.columns(2)

with col1:
    st.header('VERB')
    st.subheader('padre madre libro zapato tempeh saber sombrero')

with col2:
    st.header('NOUN')
    st.subheader('leer comer usar')

import string
# sentence = ' padre madre libro zapato tempeh saber sombrero leer comer usar'
sentence = st.text_input('')
input_string = sentence.lower() + '#' 

# initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
              'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
              'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29',
              'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36']

transition_table = {}

for state in state_list:
  for alphabet in alphabet_list:
    transition_table[(state, alphabet)] = 'error'
  transition_table[(state, '#')] = 'error'
  transition_table[(state, ' ')] = 'error'

# spaces before input string
transition_table['q0', ' '] = 'q0'

# update the transition table for the following token: padre
transition_table[('q0', 'p')] = 'q1'
transition_table[('q1', 'a')] = 'q2'
transition_table[('q2', 'd')] = 'q3'
transition_table[('q3', 'r')] = 'q4'
transition_table[('q4', 'e')] = 'q35'
transition_table[('q35', ' ')] = 'q36'
transition_table[('q35', '#')] = 'accept'
transition_table[('q36', ' ')] = 'q36'
transition_table[('q36', '#')] = 'accept'

# transition for new token
transition_table[('q36', 'p')] = 'q1'
transition_table[('q36', 'm')] = 'q5'
transition_table[('q36', 'l')] = 'q6'
transition_table[('q36', 'z')] = 'q12'
transition_table[('q36', 't')] = 'q16'
transition_table[('q36', 's')] = 'q21'
transition_table[('q36', 'c')] = 'q30'
transition_table[('q36', 'u')] = 'q33'


# update the transition table for the following token: madre
transition_table[('q0', 'm')] = 'q5'
transition_table[('q5', 'a')] = 'q2'
transition_table[('q2', 'd')] = 'q3'
transition_table[('q3', 'r')] = 'q4'
transition_table[('q4', 'e')] = 'q35'

# update the transition table for the following token: libro
transition_table[('q0', 'l')] = 'q6'
transition_table[('q6', 'i')] = 'q7'
transition_table[('q7', 'b')] = 'q8'
transition_table[('q8', 'r')] = 'q9'
transition_table[('q9', 'o')] = 'q35'


# update the transition table for the following token: leer
transition_table[('q0', 'l')] = 'q6'
transition_table[('q6', 'e')] = 'q10'
transition_table[('q10', 'e')] = 'q11'
transition_table[('q11', 'r')] = 'q35'

# update the transition table for the following token: zapato
transition_table[('q0', 'z')] = 'q12'
transition_table[('q12', 'a')] = 'q13'
transition_table[('q13', 'p')] = 'q14'
transition_table[('q14', 'a')] = 'q15'
transition_table[('q15', 't')] = 'q9'
transition_table[('q9', 'o')] = 'q35'

# update the transition table for the following token: tempeh
transition_table[('q0', 't')] = 'q16'
transition_table[('q16', 'e')] = 'q17'
transition_table[('q17', 'm')] = 'q18'
transition_table[('q18', 'p')] = 'q19'
transition_table[('q19', 'e')] = 'q20'
transition_table[('q20', 'h')] = 'q35'

# update the transition table for the following token: saber
transition_table[('q0', 's')] = 'q21'
transition_table[('q21', 'a')] = 'q22'
transition_table[('q22', 'b')] = 'q23'
transition_table[('q23', 'e')] = 'q24'
transition_table[('q24', 'r')] = 'q35'

# update the transition table for the following token: sombrero
transition_table[('q0', 's')] = 'q21'
transition_table[('q21', 'o')] = 'q25'
transition_table[('q25', 'm')] = 'q26'
transition_table[('q26', 'b')] = 'q27'
transition_table[('q27', 'r')] = 'q28'
transition_table[('q28', 'e')] = 'q29'
transition_table[('q29', 'r')] = 'q9'
transition_table[('q9', 'o')] = 'q35'

# update the transition table for the following token: comer
transition_table[('q0', 'c')] = 'q30'
transition_table[('q30', 'o')] = 'q31'
transition_table[('q31', 'm')] = 'q32'
transition_table[('q32', 'e')] = 'q11'
transition_table[('q11', 'r')] = 'q35'

# update the transition table for the following token: usar
transition_table[('q0', 'u')] = 'q33'
transition_table[('q33', 's')] = 'q34'
transition_table[('q34', 'a')] = 'q11'
transition_table[('q11', 'r')] = 'q35'


# lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state!='accept':
  current_char = input_string[idx_char]
  current_token += current_char
  state = transition_table[(state, current_char)]
  if state == 'q35':
    st.write('current token: ', current_token, ', valid')
    current_token = ''
  if sentence == '':
    break
    
  if state == 'error':
    st.write('error')
    break;
  idx_char = idx_char + 1

# conclusion
if state == 'accept':
  lexical_valid = True
else :
  lexical_valid = False

###########################3
# input example
# sentence = 'padre usar sombrero'
tokens = sentence.lower().split()
tokens.append('EOS')


# symbols definition
non_terminals = ['S', 'NN', 'VB']
terminals = ['padre', 'madre', 'libro', 'zapato', 'tempeh', 'saber', 'sombrero', 'leer', 'comer', 'usar']

# Parse table definition
parse_table = {}

parse_table[('S', 'padre')] = ['NN', 'VB', 'NN']
parse_table[('S', 'madre')] = ['NN', 'VB', 'NN']
parse_table[('S', 'libro')] = ['NN', 'VB', 'NN']
parse_table[('S', 'zapato')] = ['NN', 'VB', 'NN']
parse_table[('S', 'tempeh')] = ['NN', 'VB', 'NN']
parse_table[('S', 'saber')] = ['NN', 'VB', 'NN']
parse_table[('S', 'sombrero')] = ['NN', 'VB', 'NN']
parse_table[('S', 'leer')] = ['error']
parse_table[('S', 'comer')] = ['error']
parse_table[('S', 'usar')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'padre')] = ['padre']
parse_table[('NN', 'madre')] = ['madre']
parse_table[('NN', 'libro')] = ['libro']
parse_table[('NN', 'zapato')] = ['zapato']
parse_table[('NN', 'tempeh')] = ['tempeh']
parse_table[('NN', 'saber')] = ['saber']
parse_table[('NN', 'sombrero')] = ['sombrero']
parse_table[('NN', 'leer')] = ['error']
parse_table[('NN', 'comer')] = ['error']
parse_table[('NN', 'usar')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'padre')] = ['error']
parse_table[('VB', 'madre')] = ['error']
parse_table[('VB', 'libro')] = ['error']
parse_table[('VB', 'zapato')] = ['error']
parse_table[('VB', 'tempeh')] = ['error']
parse_table[('VB', 'saber')] = ['error']
parse_table[('VB', 'sombrero')] = ['error']
parse_table[('VB', 'leer')] = ['leer']
parse_table[('VB', 'comer')] = ['comer']
parse_table[('VB', 'usar')] = ['usar']
parse_table[('VB', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append("#")
stack.append('S')
if sentence == '':
  print()
elif lexical_valid:
  st.write('Semua token di input: "%s" Valid!\n' %(sentence))
else :
  st.write('Sentence "%s" tidak diproses karena pada lexical analyzer tidak valid.\n' %(sentence))

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]

# parsing process
if lexical_valid:
  while (len(stack) > 0):
    top = stack[len(stack)-1]
    #st.write('top = ', top)
    #st.write('symbol = ', symbol)
    if top in terminals:
      #st.write('top adalah simbol terminal')
      if top == symbol:
        stack.pop()
        idx_token += 1
        symbol = tokens[idx_token]
        if symbol == 'EOS':
          #st.write('isi stack: ', stack)
          stack.pop()
      else:
        #st.write('error')
        break;
    elif top in non_terminals:
     # st.write('top adalah simbol non-terminal')
      if parse_table[(top, symbol)][0] != 'error':
        stack.pop()
        symbols_to_be_pushed = parse_table[(top, symbol)]
        for i in range(len(symbols_to_be_pushed)-1,-1,-1):
          stack.append(symbols_to_be_pushed[i])
      else:
        st.write('error')
        break;
    else:
      st.write('error')
      break;
      st.write("\n\n")

if symbol == 'EOS' and len(stack) == 0:
      st.success('Input string "%s" diterima dan sesuai grammar!' %(sentence))
elif symbol == "EOS":
      st.write()
else:
      st.error('Error, string "%s" tidak diterima karena tidak sesuai grammar!' %(sentence)) 
