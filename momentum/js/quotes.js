const quotes = [
    {
        quote: "삶이 있는 한 희망은 있다",
        author: "키케로 ",
    },{
        quote: "언제나 현재에 집중할수 있다면 행복할것이다",
        author: "파울로 코엘료 ",
    },{
        quote: "행복의 문이 하나 닫히면 다른 문이 열린다 그러나 우리는 종종 닫힌 문을 멍하니 바라보다가 우리를 향해 열린 문을 보지 못하게 된다",
        author: "헬렌켈러",
    },{
        quote: "먼저핀꽃은 먼저진다  남보다 먼저 공을 세우려고 조급히 서둘것이 아니다",
        author: "채근담 ",
    },{
        quote: "행복한 삶을 살기위해 필요한 것은 거의 없다",
        author: "마르쿠스 아우렐리우스 안토니우스",
    },{
        quote: "절대 어제를 후회하지 마라 . 인생은 오늘의 나 안에 있고 내일은 스스로 만드는 것이다 ",
        author: "L.론허바드 ",
    },{
        quote: "너무 소심하고 까다롭게 자신의 행동을 고민하지 말라 . 모든 인생은 실험이다 . 더많이 실험할수록 더나아진다",
        author: "랄프 왈도 에머슨",
    },{
        quote: "한번의 실패와 영원한 실패를 혼동하지 마라",
        author: "F.스콧 핏제랄드 ",
    },{
        quote: "행복은 습관이다,그것을 몸에 지니라",
        author: "허버드",
    },{
        quote: "고개 숙이지 마십시오. 세상을 똑바로 정면으로 바라보십시오",
        author: "헬렌 켈러",
    }
]

const quote = document.querySelector('#quote span:first-child');
const author = document.querySelector('#quote span:last-child');

const todaysQuote = quotes[Math.floor(Math.random()*quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;





