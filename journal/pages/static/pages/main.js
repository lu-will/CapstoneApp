// $(document).ready(function(){
//     $('.datepicker').datepicker();
//   });

// const Calender = document.querySelector('.datepicker')
// M.Datapicker.init(Calender, {
//   format: 'dd/mmmm/yy'
// })

var currYear = (new Date()).getFullYear();

$(document).ready(function() {
  $(".datepicker").datepicker({
    defaultDate: new Date(),
    // setDefaultDate: new Date(2000,01,31),
    // maxDate: new Date(currYear),
    // yearRange: [1928, currYear],
    format: "yyyy-mm-dd"    
  });
});


$(document).ready(function(){
 
    $('.collapsible').collapsible();
 
  });