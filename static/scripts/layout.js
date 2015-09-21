
'use strict';

var lastScrollTop = 0,
  offset,
  direction;

function scrollDirection() {
    offset = window.pageYOffset;

    if (offset > lastScrollTop) {
      direction = 'down';
    }
    else {
      direction = 'up';
    }

    lastScrollTop = offset;
    return  direction;
}

$(window).bind( 'scroll', function() {
  var scroll = $(window).scrollTop();

  var dir = scrollDirection();
  if( scroll > 500 && dir === 'down' )  {
    $( '.navbar' ).slideDown( 10, 'easeOutSine' );
    $( '.navbar' ).removeClass( 'hide' );
  } else {
    $( '.navbar' ).slideUp( 100, 'easeOutSine' );
  }
});
