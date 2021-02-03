let lastno = '0';

function getchat() {
    $.ajax({
        type: 'GET',
        url: 'chatlist',
        data: {
            "lastno" : lastno
        },
        dataType: 'JSON',
        success: function (data) {
            // console.log("성공은 함");
            //순위 테이블 받아와야함 
            // console.log('success')
            var chatlist = data.result2;
            var o = document.getElementById('list');
            var dd;

            // 채팅내용 추가
            for (var i = 0; i < chatlist.length; i++) {
                dd = document.createElement('dd');
                dd.appendChild(document.createTextNode(chatlist[i].msg));
                o.appendChild(dd);
            }

            // 가장 아래로 스크롤
            o.scrollTop = o.scrollHeight;

            lastno = data.lastno;
  
            console.log(lastno);
            // body += "<tbody></tbody>";
            // body2 += "<tbody></tbody>";
            // $("#list").html(head + body);
            // $("#list2").html(head2 + body2);


        },
        error: function (request, status, error) {
            alert('통신 실패')
        }
    })

};

var timer;

function init() {
    getchat();
    // 최초에 함수를 한번 실행시켜주고 
    timer = setInterval(getchat, 1000);
    // setInterval이라는 함수로 매초마다 실행을 해줍니다.
    // setInterval은 첫번째 파라메터는 함수이고 두번째는 시간인데 밀리초단위로 받습니다. 1000 = 1초 
}
init();
