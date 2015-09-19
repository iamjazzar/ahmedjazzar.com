
"use strict";

// toggle nav menu
$( "#toggle" ).click(function() {
  $(this).toggleClass( "active" );
  $( "#overlay" ).toggleClass( "open" );
});

// scroll top hover

$(".scroll-top").hover(
  function () {
    $( ".fa-angle-up" ).toggleClass( "floating" );
});

// scroll to top
$("a[href^='#header']").on( "click", function(e) {

   e.preventDefault();
   var hash = this.hash;

   $( "body" ).animate({
       scrollTop: $(hash).offset().top
     }, 1000, function(){
   });
 });
