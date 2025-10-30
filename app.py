import streamlit as st
import streamlit.components.v1 as components
import os # 파일 경로를 다루기 위해 import

# --- 페이지 설정 ---
# 이 코드는 항상 가장 먼저 실행되어야 합니다.
st.set_page_config(
    page_title="미션: 아이디어를 코드로",  # 브라우저 탭에 표시될 제목
    layout="wide",                       # 콘텐츠를 전체 너비로 표시
    initial_sidebar_state="collapsed"    # 사이드바를 기본적으로 숨김
)

# --- HTML 파일 로드 ---

# HTML 파일이 위치한 경로를 정확히 지정합니다.
# 'htmls' 폴더 내의 'index.html'
html_file_path = os.path.join('htmls', 'index.html')

# --- HTML 렌더링 ---
try:
    # 'utf-8' 인코딩으로 HTML 파일을 엽니다. (한글 깨짐 방지)
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Streamlit 컴포넌트를 사용해 HTML을 렌더링합니다.
    # height를 매우 크게 설정하여 HTML 페이지 전체가 보이도록 하고,
    # Streamlit 앱의 메인 스크롤을 사용하도록 유도합니다. (이중 스크롤바 방지)
    components.html(html_content, height=5000, scrolling=False)

except FileNotFoundError:
    st.error("ERROR: 'htmls/index.html' 파일을 찾을 수 없습니다.")
    st.warning("app.py 파일과 동일한 위치에 'htmls' 폴더를 만들고, 그 안에 'index.html' 파일을 넣어주세요.")
except Exception as e:
    st.error(f"파일 로드 중 알 수 없는 오류가 발생했습니다: {e}")
