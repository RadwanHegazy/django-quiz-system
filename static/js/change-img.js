
var imgFile = document.getElementById('imgFile');
var imgView = document.getElementById('imgView');
var imgBtn = document.getElementById('imgBtn');

imgBtn.addEventListener('click',()=>{
    imgFile.click()
})

imgFile.addEventListener('change',(e)=>{
    var img_path = URL.createObjectURL(e.target.files[0]);

    imgView.src = img_path
})