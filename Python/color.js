var Links = {
  setColor:function(color){
    var alist = document.querySelectorAll('a');
    i = 0;
    while(i < alist.length){
    alist[i].style.color = color;
    i = i + 1;
    }

  }
}
var Body = {
  setColor:function(color){
  document.querySelector('body').style.color= color;
  },
  setBackgroundColor:function(color){
  document.querySelector('body').style.backgroundColor= color;
  }
}
  function night_dayHandller(self){
    var target = document.querySelector('body');
    if(self.value ==='NIGHT'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    self.value ='DAY';
    Links.setColor('yellow');
  }

  else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    self.value ='NIGHT';
    Links.setColor('blue');

    }
  }
