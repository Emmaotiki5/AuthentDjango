from anikimiapi import AniKimi


Kimi = AniKimi(
    gogoanime_token="f3rdbg8ktqnq4am5l0t5md16q1",
    auth_token="jc8gXLpIxS%2Fl2e3txA7WDzaLtdQuos6rRsJsHMhCjzFUZ9VJGUhgcDvFea9I0o%2FuG%2FCEgsDGT7OkU37ukPMAfA%3D%3D",
    host="https://gogoanime.hu/"  
)

anime_link = Kimi.get_episode_link_basic(animeid="clannad", episode_num=3)

print(anime_link.link_hdp)
