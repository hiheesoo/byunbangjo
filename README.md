# byunbangjo

## 수정사항
- 10/20 방성준
    - 영화 create, detail 기능 구현 및 디버깅
    - index(main page)
        - DB에 영화 있을 시 
            - 있는 영화 전부 출력
        - DB에 영화 없을 시
            - 생성 버튼(create)
        - 좋아요, 싫어요 기능 구현
- 10/21 방성준
    - 접속 시 바로 movies.index로 redirect
    - comment를 text field에서 char field로 변경
    - detail page 디버깅
      - detail 페이지에서 좋아요, 싫어요 확인 가능
      - 댓글 작성, 삭제 기능 추가
      - 영화에 맞는 댓글만 보이게 수정완료
    - CSS 다듬기
      - index 페이지 화면 lg 이상이면 영화 카드 2개씩 출력
      - nav바 로그인 시 로고 멘트 수정
      - 카드 형식으로 댓글 출력, detail 페이지 다듬기