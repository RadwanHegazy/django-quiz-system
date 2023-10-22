
var questions = '';
var index = 0 ;


$.ajax({
    type:"GET",
    url:".",
    data:{'api':true},
    success:function(data){
        questions = data;
        UpdateQuestionView(0)
    }
})


var user_answers = [];

var title = document.querySelector('.info .title');
var select = document.querySelector('.enter-data select');


function UpdateQuestionView(index){
var current_q = questions[index]

var options = `
    <option value="1" >${current_q['a_1']}</option>
    <option value="2">${current_q['a_2']}</option>
    <option value="3">${current_q['a_3']}</option>
    <option value="4">${current_q['a_4']}</option>
`;

select.querySelectorAll('option').forEach(i=>i.remove());

select.id = current_q['uuid']    
title.textContent = current_q['q_title']
select.innerHTML += options;

}




var next_btn = document.getElementById('next');
var prev_btn = document.getElementById('prev');

next_btn.addEventListener('click',()=>{

index++
AppendToUserAnswer()
if (index < questions.length){
    UpdateQuestionView(index)
}else{
    index--
}

})

prev_btn.addEventListener('click',()=>{

index--
AppendToUserAnswer()

if (index >= 0){
    UpdateQuestionView(index)
}else{
    index++
}

})

select.addEventListener('change',()=>{

AppendToUserAnswer();

})

select.addEventListener('click',()=>{

AppendToUserAnswer();

})


function AppendToUserAnswer () {
    

    user_answers.push({
        'question_uuid' : select.id,
        'user_answer' : select.value
    })
    
    

    
}



function SendData () {

    var q_id = [];
    var x = [];

    user_answers.reverse().forEach( i => {

        if (q_id.includes(i['question_uuid']) == false){
            x.push(i)
            q_id.push(i['question_uuid'])
        };

    })

    $.ajax({
        type:"POST",
        url:"/check/", 
        data:{
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            'answers':JSON.stringify(x),
            'student_uuid':document.getElementById('student').value,
            'quiz_uuid': document.getElementById('quiz_uuid').value
        },success:function(done_url){
            window.location.href = done_url;
        }
    })

}



document.querySelector('.tables .main-button').addEventListener('click',()=>{

    var conf = confirm('هل انت متأكد من التسليم ؟')

    if (conf){
        SendData();
    }


})