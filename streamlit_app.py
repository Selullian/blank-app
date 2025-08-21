# 파일명: streamlit_app.py
# 실행: 터미널에서 streamlit run streamlit_app.py 입력

import streamlit as st

# --- 초기 설정 ---
st.set_page_config(layout="wide")

st.title("🎲 틱택토 (Tic-Tac-Toe)")
st.write("플레이어 X와 O가 번갈아가며 칸을 클릭하세요.")

# --- CSS를 이용한 버튼 스타일 수정 ---
# height 값을 100px에서 60px로 줄여서 버튼을 더 납작하게 만듭니다.
st.markdown("""
<style>
    div.stButton > button {
        width: 200%;
        height: 60px; /* 세로 길이를 여기에서 수정 */
        font-size: 2.5em;
    }
</style>
""", unsafe_allow_html=True)


# --- 게임 상태 초기화 ---
if "board" not in st.session_state:
    st.session_state.board = ["\u00A0"] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# --- 승자 판별 함수 ---
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
        [0, 4, 8], [2, 4, 6]             # 대각선
    ]
    for a, b, c in win_conditions:
        if board[a] != "\u00A0" and board[a] == board[b] == board[c]:
            return board[a]
    return None

# --- 보드 그리기 및 클릭 로직 처리 ---
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        if cols[col].button(st.session_state.board[idx], key=f"cell{idx}"):
            if st.session_state.board[idx] == "\u00A0" and not st.session_state.winner:
                st.session_state.board[idx] = st.session_state.current_player
                st.session_state.winner = check_winner(st.session_state.board)
                if not st.session_state.winner:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                st.rerun()

# --- 결과 출력 ---
if st.session_state.winner:
    st.success(f"🎉 승자: {st.session_state.winner}")
elif "\u00A0" not in st.session_state.board:
    st.warning("🤝 무승부!")

# --- 다시 시작 버튼 ---
if st.button("🔄 다시 시작"):
    st.session_state.board = ["\u00A0"] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.rerun()