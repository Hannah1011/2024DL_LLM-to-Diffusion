import pathlib
import textwrap
import google.generativeai as genai
import google.generativeai as genai

GOOGLE_API_KEY= 'GOOGLE_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)

# 모델 초기화
def LLM(text):
  model = genai.GenerativeModel('gemini-pro')
  while True:
    user_input = text
    if user_input=="q":
      break
    # 프롬프트와 instruction 정의
    else:
      instruction = """ 당신은 대규모 패션 이미지 데이터셋을 활용해 의상 스타일을 변경하는 AI 시스템을 개발 중인 엔지니어입니다.
                        시스템은 사용자의 요청에 따라 의상 스타일과 색상을 변경하고, 이를 JSON 형식으로 출력하도록 설계되어야 합니다."""
      prompt = """
      [사용자 요청 처리 규칙]
      1.	사용자의 요청에 따라 의상의 종류와 색상을 추출하세요.
      2.	요청에서 상의(top)와 하의(bottom)에 해당하는 키워드를 각각 추출하여 JSON 형식으로 반환합니다.
      •	예외: one piece와 dress는 상의(top)로 간주합니다.
      3.	추출된 결과가 없으면 빈 문자열로 남깁니다.

      [JSON 출력 규칙]
        1.	출력 형식: {"top": ["색상", "문양", "종류"], "bottom": ["색상","문양", "종류"]}
        2.	키워드가 없는 경우 해당 항목을 빈 문자열로 남깁니다.
        •	예: {"top": ["", "shirt"], "bottom": ["", ""]}
      [사용자 예시 요청 및 응답]
      사용자: 여자의 상의를 파란 꽃무늬 스웨트셔츠로, 하의를 검은 스커트로 바꿔줘.  
      응답: {"top": ["파란", "꽃무늬", "스웨트셔츠"], "bottom": ["검은", "", "스커트"]}  

      사용자: 셔츠로 바꿔줘.  
      응답: {"top": ["", "","셔츠"], "bottom": ["", "", ""]}  

      사용자: 드레스 색상을 빨간색으로 바꾸고 반짝이는 재질로 바꿔줘.  
      응답: {"top": ["빨간", "반짝이는 재질", "드레스"], "bottom": ["","", ""]}  

      사용자: 하의를 청바지로 바꿔줘.  
      응답: {"top": ["","", ""], "bottom": ["", "", "청바지"]}
      """

      # 전체 프롬프트 생성 (instruction 포함)
      full_prompt = f"{instruction}\n{prompt}{user_input}\n  You: "

      # 모델 호출
      response = model.generate_content(full_prompt)

      # 응답 출력
      return response
