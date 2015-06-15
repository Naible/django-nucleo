'use strict';

angular.module('angularDjangoRegistrationAuthApp')
  .controller('LoginCtrl', function ($scope, $location, djangoAuth, Validate) {
    $scope.model = {'username':'','password':''};
  	$scope.complete = false;
    $scope.login = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.login($scope.model.username, $scope.model.password)
        .then(function(data){
        	// success case
        	$location.path("/");
        },function(data){
        	// error case
        	$scope.errors = data;
        });
      }
    }
    $scope.loginFacebook = function(){
      function popupWindow(url, title, width, height) {
        width = width || 1150;
        height = height || 650;
        var left = (screen.width/2)-(width/2);
        var top = (screen.height/2)-(height/2);
        var windowParams = 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, ' +
            'resizable=no, copyhistory=no, width='+width+', height='+height+', top='+top+', left='+left;
        return window.open(url, title, windowParams);
      }

      var url = '/account/facebook/login/?process=login';
      var title = 'Login with Facebook';
      popupWindow(url, title);
      window.resizeTo($(document.body).width(), $(document.body).height());
    }
  });
