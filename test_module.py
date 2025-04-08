# import streamlit as st
# import time
# import random
# import pandas as pd

# sentences = {
#     "Easy": ["Python is fun.", "I love coding."],
#     "Medium": ["The quick brown fox jumps over the lazy dog."],
#     "Hard": ["Debugging is twice as hard as writing the code."]
# }

# def run_typing_test():
#     st.header("🎯 Typing Speed Test")
#     name = st.text_input("Enter your name:")
#     level = st.selectbox("Choose difficulty", list(sentences.keys()))
#     sentence = random.choice(sentences[level])
#     st.markdown(f"**Type this:** `{sentence}`")
    
#     input_text = st.text_area("Start typing here:", height=150)
#     if "start_time" not in st.session_state:
#         if input_text:
#             st.session_state.start_time = time.time()

#     if st.button("Submit"):
#         if input_text.strip():
#             end_time = time.time()
#             elapsed = end_time - st.session_state.start_time
#             words = len(input_text.split())
#             wpm = round((words / elapsed) * 60, 2)
#             accuracy = round(sum(1 for a, b in zip(input_text, sentence) if a == b) / len(sentence) * 100, 2)
#             st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")
            
#             # Save data
#             df = pd.DataFrame([{"name": name, "speed": wpm, "accuracy": accuracy, "difficulty": level}])
#             df.to_csv("user_data.csv", mode='a', header=False, index=False)

#             del st.session_state.start_time
#         else:
#             st.warning("Please type the sentence.")


# import streamlit as st
# st.set_page_config(page_title="Typing Speed Pro", layout="wide")  # ✅ FIRST Streamlit command

# import time
# import random
# import pandas as pd

# # Now it's safe to use other Streamlit commands
# st.title("🔥 Typing Speed Test")


# # Predefined sentence pools
# sentences = {
#     "Easy": ["Python is fun.", "I love coding."],
#     "Medium": ["The quick brown fox jumps over the lazy dog."],
#     "Hard": ["Debugging is twice as hard as writing the code."]
# }

# def run_typing_test():
#     st.header("🎯 Typing Speed Test")
#     name = st.text_input("Enter your name:")

#     # Add custom difficulty option
#     level = st.selectbox("Choose difficulty", list(sentences.keys()) + ["Custom"])
#     custom_sentence = ""
    
#     # Determine sentence to use
#     if level == "Custom":
#         custom_sentence = st.text_area("Enter your custom text here:")
#         sentence = custom_sentence.strip()
#     else:
#         sentence = random.choice(sentences[level])

#     if sentence:
#         st.markdown(f"**Type this:** `{sentence}`")

#         if "typing_input" not in st.session_state:
#             st.session_state.typing_input = ""

#         st.session_state.typing_input = st.text_area("Start typing here:", value=st.session_state.typing_input, height=150)

#         # Set timer when typing starts
#         if "start_time" not in st.session_state and st.session_state.typing_input:
#             st.session_state.start_time = time.time()

#         col1, col2 = st.columns(2)

#         # Submit button
#         if col1.button("Submit"):
#             if st.session_state.typing_input.strip():
#                 end_time = time.time()
#                 elapsed = end_time - st.session_state.start_time
#                 words = len(st.session_state.typing_input.split())
#                 wpm = round((words / elapsed) * 60, 2)
#                 accuracy = round(sum(1 for a, b in zip(st.session_state.typing_input, sentence) if a == b) / len(sentence) * 100, 2)
#                 st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")

#                 # Save data
#                 df = pd.DataFrame([{"name": name, "speed": wpm, "accuracy": accuracy, "difficulty": level}])
#                 df.to_csv("user_data.csv", mode='a', header=False, index=False)

#                 # Reset session values
#                 del st.session_state.start_time
#                 st.session_state.typing_input = ""
#             else:
#                 st.warning("Please type the sentence.")

#         # Reset button
#         if col2.button("Reset"):
#             if "start_time" in st.session_state:
#                 del st.session_state.start_time
#             st.session_state.typing_input = ""
#             st.rerun() 

# # Run the test
# run_typing_test()


# import streamlit as st
# st.set_page_config(page_title="Typing Speed Pro", layout="wide")  # ✅ First Streamlit command
# import time
# import random
# import pandas as pd

# # Now it's safe to use other Streamlit commands
# st.title("🔥 Typing Speed Test")

# # Sentence pool
# sentences = {
#     "Easy": ["Python is fun.", "I love coding."],
#     "Medium": ["The quick brown fox jumps over the lazy dog."],
#     "Hard": ["Debugging is twice as hard as writing the code."]
# }

# def run_typing_test():
#     st.header("🎯 Typing Speed Test")
#     name = st.text_input("Enter your name:")

#     # Difficulty and Custom Input
#     level = st.selectbox("Choose difficulty", list(sentences.keys()) + ["Custom"])
#     sentence = ""

#     if level == "Custom":
#         custom_sentence = st.text_area("✍️ Enter your custom text here:")
#         if custom_sentence.strip():
#             sentence = custom_sentence.strip()
#         else:
#             st.info("Please enter some custom text to proceed.")
#     else:
#         sentence = random.choice(sentences[level])

#     if sentence:
#         st.markdown(f"**Type this:** `{sentence}`")

#         if "typing_input" not in st.session_state:
#             st.session_state.typing_input = ""

#         st.session_state.typing_input = st.text_area(
#             "Start typing here:", 
#             value=st.session_state.typing_input, 
#             height=150
#         )

#         # Start time when typing begins
#         if "start_time" not in st.session_state and st.session_state.typing_input:
#             st.session_state.start_time = time.time()

#         col1, col2 = st.columns(2)

#         # Submit button
#         if col1.button("Submit"):
#             if st.session_state.typing_input.strip():
#                 end_time = time.time()
#                 elapsed = end_time - st.session_state.start_time
#                 words = len(st.session_state.typing_input.split())
#                 wpm = round((words / elapsed) * 60, 2)
#                 accuracy = round(
#                     sum(1 for a, b in zip(st.session_state.typing_input, sentence) if a == b) 
#                     / len(sentence) * 100, 2
#                 )
#                 st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")

#                 # Save results
#                 df = pd.DataFrame([{
#                     "name": name, 
#                     "speed": wpm, 
#                     "accuracy": accuracy, 
#                     "difficulty": level
#                 }])
#                 df.to_csv("user_data.csv", mode='a', header=False, index=False)

#                 # Reset
#                 del st.session_state.start_time
#                 st.session_state.typing_input = ""
#             else:
#                 st.warning("Please type the sentence.")

#         # Reset button
#         if col2.button("Reset"):
#             if "start_time" in st.session_state:
#                 del st.session_state.start_time
#             st.session_state.typing_input = ""
#             st.rerun()

# # Run the test
# run_typing_test()
# import streamlit as st
# import time
# import random
# import pandas as pd

# sentences = {
#     "Easy": ["Python is fun.", "I love coding."],
#     "Medium": ["The quick brown fox jumps over the lazy dog."],
#     "Hard": ["Debugging is twice as hard as writing the code."]
# }

# def run_typing_test():
#     st.header("🎯 Typing Speed Test")

#     name = st.text_input("Enter your name:")
#     level = st.selectbox("Choose difficulty", list(sentences.keys()) + ["Custom"])

#     sentence = ""
#     if level == "Custom":
#         custom_sentence = st.text_area("Enter your custom text here:")
#         sentence = custom_sentence.strip()
#     else:
#         sentence = random.choice(sentences[level])

#     if sentence:
#         st.markdown(f"**Type this:** `{sentence}`")

#         # Control test start
#         if "test_started" not in st.session_state:
#             st.session_state.test_started = False
#         if "start_time" not in st.session_state:
#             st.session_state.start_time = 0

#         if not st.session_state.test_started:
#             if st.button("Start Test"):
#                 st.session_state.test_started = True
#                 st.session_state.start_time = time.time()
#                 st.session_state.typing_input = ""
#                 st.rerun()
#             return

#         st.session_state.typing_input = st.text_area("Start typing here:", value=st.session_state.typing_input, height=150)

#         col1, col2 = st.columns(2)

#         if col1.button("Submit"):
#             if st.session_state.typing_input.strip():
#                 end_time = time.time()
#                 elapsed = end_time - st.session_state.start_time
#                 words = len(st.session_state.typing_input.split())
#                 wpm = round((words / elapsed) * 60, 2)
#                 accuracy = round(sum(1 for a, b in zip(st.session_state.typing_input, sentence) if a == b) / len(sentence) * 100, 2)
#                 st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")

#                 # Save result
#                 df = pd.DataFrame([{"name": name, "speed": wpm, "accuracy": accuracy, "difficulty": level}])
#                 df.to_csv("user_data.csv", mode='a', header=False, index=False)

#                 # Reset test state
#                 st.session_state.test_started = False
#                 st.session_state.typing_input = ""
#                 st.session_state.start_time = 0
#             else:
#                 st.warning("Please type the sentence.")

#         if col2.button("Reset"):
#             st.session_state.test_started = False
#             st.session_state.typing_input = ""
#             st.session_state.start_time = 0
#             st.rerun()
# import streamlit as st
# import time
# import random
# import pandas as pd

# # Sentences by difficulty
# sentences = {
#     "Easy": ["Python is fun.", "I love coding."],
#     "Medium": ["The quick brown fox jumps over the lazy dog."],
#     "Hard": ["Debugging is twice as hard as writing the code."]
# }

# def run_typing_test():
#     st.header("🎯 Typing Speed Test")

#     name = st.text_input("Enter your name:")
#     level = st.selectbox("Choose difficulty", list(sentences.keys()) + ["Custom"])

#     sentence = ""
#     if level == "Custom":
#         custom_sentence = st.text_area("Enter your custom text here:")
#         sentence = custom_sentence.strip()
#     else:
#         sentence = random.choice(sentences[level])

#     if sentence:
#         st.markdown(f"**Type this:** `{sentence}`")

#         # Session state initialization
#         if "test_started" not in st.session_state:
#             st.session_state.test_started = False
#         if "start_time" not in st.session_state:
#             st.session_state.start_time = 0

#         if not st.session_state.test_started:
#             if st.button("Start Test"):
#                 st.session_state.test_started = True
#                 st.session_state.start_time = time.time()
#                 st.session_state.typing_input = ""
#                 st.rerun()
#             return

#         st.session_state.typing_input = st.text_area("Start typing here:", value=st.session_state.typing_input, height=150)

#         col1, col2 = st.columns(2)

#         if col1.button("Submit"):
#             if st.session_state.typing_input.strip():
#                 end_time = time.time()
#                 elapsed = end_time - st.session_state.start_time
#                 words = len(st.session_state.typing_input.split())
#                 wpm = round((words / elapsed) * 60, 2)
#                 accuracy = round(
#                     sum(1 for a, b in zip(st.session_state.typing_input, sentence) if a == b) / len(sentence) * 100, 2
#                 )
#                 total_chars = len(st.session_state.typing_input)

#                 st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")
#                 st.info(f"📝 Total Characters Typed (with spaces, special chars): {total_chars}")

#                 # Save result
#                 df = pd.DataFrame([{
#                     "name": name,
#                     "speed": wpm,
#                     "accuracy": accuracy,
#                     "difficulty": level,
#                     "characters_typed": total_chars
#                 }])
#                 df.to_csv("user_data.csv", mode='a', header=False, index=False)

#                 # Reset state
#                 st.session_state.test_started = False
#                 st.session_state.typing_input = ""
#                 st.session_state.start_time = 0
#             else:
#                 st.warning("Please type the sentence.")

#         if col2.button("Reset"):
#             st.session_state.test_started = False
#             st.session_state.typing_input = ""
#             st.session_state.start_time = 0
#             st.rerun()

# # Run the app
# run_typing_test()
import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime
import os

# Safe path to save CSV
SAVE_PATH = "C:/Users/gouta/Documents/user_data.csv"

# Sentences by difficulty
sentences = {
    "Easy": ["Python is fun.", "I love coding."],
    "Medium": ["The quick brown fox jumps over the lazy dog."],
    "Hard": ["Debugging is twice as hard as writing the code."]
}

def run_typing_test():
    st.header("🎯 Typing Speed Test")

    name = st.text_input("Enter your name:")
    level = st.selectbox("Choose difficulty", list(sentences.keys()) + ["Custom"])

    sentence = ""
    if level == "Custom":
        custom_sentence = st.text_area("Enter your custom text here:")
        sentence = custom_sentence.strip()
    else:
        sentence = random.choice(sentences[level])

    if sentence:
        st.markdown(f"**Type this:** `{sentence}`")

        # Session state init
        if "test_started" not in st.session_state:
            st.session_state.test_started = False
        if "start_time" not in st.session_state:
            st.session_state.start_time = 0

        if not st.session_state.test_started:
            if st.button("Start Test"):
                st.session_state.test_started = True
                st.session_state.start_time = time.time()
                st.session_state.typing_input = ""
                st.rerun()
            return

        st.session_state.typing_input = st.text_area("Start typing here:", value=st.session_state.typing_input, height=150)

        col1, col2 = st.columns(2)

        if col1.button("Submit"):
            if st.session_state.typing_input.strip():
                end_time = time.time()
                elapsed = end_time - st.session_state.start_time
                words = len(st.session_state.typing_input.split())
                wpm = round((words / elapsed) * 60, 2)
                accuracy = round(
                    sum(1 for a, b in zip(st.session_state.typing_input, sentence) if a == b) / len(sentence) * 100, 2
                )
                total_chars = len(st.session_state.typing_input)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                st.success(f"⏱ Time: {int(elapsed)}s | 🧠 Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%")
                st.info(f"📝 Total Characters Typed (with spaces, special chars): {total_chars}")

                # Save result
                df = pd.DataFrame([{
                    "name": name,
                    "speed": wpm,
                    "accuracy": accuracy,
                    "difficulty": level,
                    "characters_typed": total_chars,
                    "timestamp": timestamp
                }])
                df.to_csv(SAVE_PATH, mode='a', header=not os.path.exists(SAVE_PATH), index=False)

                # Reset state
                st.session_state.test_started = False
                st.session_state.typing_input = ""
                st.session_state.start_time = 0
            else:
                st.warning("Please type the sentence.")

        if col2.button("Reset"):
            st.session_state.test_started = False
            st.session_state.typing_input = ""
            st.session_state.start_time = 0
            st.rerun()

run_typing_test()
