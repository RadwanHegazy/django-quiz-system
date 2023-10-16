
// change between login and regsiter layers
var btnViewLayers = document.querySelectorAll('.btns button');
var container = document.querySelector('.container');

btnViewLayers.forEach( btn => {

    
    btn.addEventListener('click',(e)=>{
        btnViewLayers.forEach(i=>{i.classList.remove('active')});
        
        btn.classList.add('active')
        var ViewThisLayer = btn.id;

        container.className = "container";
        container.classList.add(ViewThisLayer);
    })

})


// // choose img in register layer

// var imgFile = document.getElementById('imgFile');
// var imgView = document.getElementById('imgView');
// var imgBtn = document.getElementById('imgBtn');

// imgBtn.addEventListener('click',()=>{
//     imgFile.click()
// })

// imgFile.addEventListener('change',(e)=>{
//     var img_path = URL.createObjectURL(e.target.files[0]);

//     imgView.src = img_path
// })