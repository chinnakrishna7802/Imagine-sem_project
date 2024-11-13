// Declaring all the necessary variables
const file = document.getElementById('file');
const preview_container= document.getElementById('preview_container');
const output_container= document.getElementById('output_container');
const preview = document.getElementById('preview');
const arrow_image = document.getElementById('arrow_image');
const output_image = document.getElementById('output_image');
const preview_text = document.getElementById('preview_text');
const output_text = document.getElementById('output_text');
const process_button=document.getElementById('process')
const dimension=window.matchMedia('(max-width:1000px)')
const refresh =document.getElementById('refresh')
// Event listener to display the preview of the uploaded image
file.addEventListener('change', function () {
    preview_container.style.display='inline-block'
    preview.src = URL.createObjectURL(this.files[0]);
    preview.style.borderRadius = '10px'
    preview.style.padding = '7px'
}, false);

// Event listener for displaying the arrow
file.addEventListener('change', function () {
    // arrow_image.style.display='inline-block'
    // arrow_image.style.width='150px'
    // arrow_image.style.height='150px'
    process_button.style.display='inline-block'
    process_button.style.margin='0rem 2rem'
    if(dimension.matches)
    {
        process_button.style.margin='2rem 0rem'
    }
}, false);

//  Event listener to display the output/enchanced form of the uploaded image
process_button.addEventListener('click', function () {
    refresh.style.display='inline-block'
    output_container.style.display='inline-block'
    output_image.src = 'hd_image.jpg';
    output_image.style.borderRadius = '10px'
    output_image.style.padding = '7px'
  }, false);
// file.addEventListener('change', function () {
//     output_container.style.display='inline-block'
//     output_image.src = URL.createObjectURL(this.files[0]);
//     output_image.style.borderRadius = '10px'
//     output_image.style.padding = '7px'
//   }, false);

refresh.addEventListener('click',()=>{
    location.reload()
})