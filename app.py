import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "⚪️",
    "불꽃": "🔥",
    "물": "💧",
    "전기": "⚡",
    "풀": "🌿",
    "얼음": "❄️",
    "격투": "🥊",
    "독": "☠️",
    "땅": "🟫",
    "비행": "🪽",
    "에스퍼": "🥄",
    "벌레": "🐛",
    "바위": "🪨",
    "고스트": "👻",
    "드래곤": "🐉",
    "악": "😈",
    "강철": "⚙️",
    "페어리": "🧚"
}

pokemons = [
     {
    "name": "피카츄",
    "types": ["전기"],
    "image_url": "https://i.namu.wiki/i/SVMK4eZf-H5dqybpTkReUG_iVr3Q4HXCPAd0lNPldimJlp41N_pCilPiR6QPghJgck28w_GgXdMAMrmnxo8-sUpYXAo1UDzu-daukUlLu22_BK9_sPRAmpgDWKE8QtCpMYFqyPpx1SWRtZlEk11Nfw.webp"
    },
    {
    "name": "누오",
    "types": ["물", "땅"],
    "image_url": "https://i.namu.wiki/i/cDs6f1XZ8NqV0ieTNWrvDYxlOAqbAyM6cFwwMzdfckacs80Q7e0OrX7UYqlGOe8a-okHmHyFSRDJxJXcUgEjHTeTOAIfwazRyVdFYse5SgMl1Lrz66i2Ykkk4VFFbvvhTr-3tjzZg5TfxyML4iRCzQ.webp"
    },
    {
    "name": "갸라도스",
    "types": ["물", "비행"],
    "image_url": "https://i.namu.wiki/i/h9WMq1hyKoT5aR1WBmDCQSyGMKk-0UWSFw8GwDXYJyf1SGP7j6eA9txN_qZyzau6rOU4cW49X7Uv13wa6etYydkgvYJfH14KfW8UBgnB6DZUvgxJJzmVQ40RXVf63Lz7oLfSpSinJZkVWPo-K-OWXQ.webp"
    },
        {
    "name": "개굴닌자",
    "types": ["물"],
    "image_url": "https://i.namu.wiki/i/2F-rWTt3FgKRh1h3SXItaa3xJWqtvdL714IKJ9DUnvtODZ4Y4mG0Ih4eULl_srIfL9_iLrtr1uFH9wYJpeDyStOlWrjhP1e936ctm_E6HCnn4KdARkXoTlhWRXAs6EhXg0o3CEONCYiQIU3HOVuRoA.webp"
    },
    {
    "name": "루카리오",
    "types": ["격투", "강철"],
    "image_url": "https://i.namu.wiki/i/_-_1FO_ztYci7Ji1iWJlmmJ15OufdWfEs91pm_fdSMnTUTOIIYFtAaTyKoxv0bXVmLwEXwM2uS_em0EvoPT7ZtLN5QmZvr6VzeS3vGPzDZzEqnimVFM7l671VVysfBsC4YE-P-cwU_xoyVcbnsbCiQ.webp"
    },  
    {
    "name": "에이스번",
    "types": ["불꽃"],
    "image_url": "https://i.namu.wiki/i/p7HMCkYJDeuETRy-Hevp7Hq5DygTQBwaLbloLFnGl8726Xti-TNP-3lk8g34bvqL-4b0t2ya57scGmPoWQYQ4VW4EdZVInzX17vdv3YbYG3-Od4bE3ZlT6wmlm4vBUHix-Vfmx5nMLgPsvbjN6F0VA.webp"
    }
]

# 포켓몬 추가 버튼
with st.form(key="form"):
    col1, col2 = st.columns(2)
    # 이름 입력
    with col1:
        name = st.text_input(label="포켓몬 이름")
    # 타입 선택
    with col2:
        types = st.multiselect(
            label="포켓몬 타입",
            options=list(type_emoji_dict.keys()),
            # 타입은 2개까지만
            max_selections=2
        )
    # 이미지 추가하기
    image_url = st.text_input(label="포켓몬 이미지 URL")
    # 업로드
    submit = st.form_submit_button(label="Submit")
    if submit:
        # 전부 입력해야 업로드 되도록 예외 처리
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓먼의 타입을 적어도 한 개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            pokemons.append({
                "name": name,
                "types": types,
                # 이미지가 있을 때는 이미지, 없으면 기본이미지
                "image_url": image_url if image_url else "./images/default.png"
            })


# 포켓몬을 이름/이미지/타입 출력
for i in range(0, len(pokemons), 3):
    # 3개씩 번호대로 출력
    row_pokemons = pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+1+j}. {pokemon['name']}**", expanded = True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))        
