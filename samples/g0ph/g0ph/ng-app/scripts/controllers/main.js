'use strict';

angular.module('angularDjangoRegistrationAuthApp')
  .controller('MainCtrl', function ($scope, $cookies, $location, djangoAuth, $http, Validate) {
    
    $scope.login = function(){
      djangoAuth.login(prompt('Username'),prompt('password'))
      .then(function(data){
        handleSuccess(data);
      },handleError);
    }
    
    $scope.logout = function(){
      djangoAuth.logout()
      .then(handleSuccess,handleError);
    }
    
    $scope.resetPassword = function(){
      djangoAuth.resetPassword(prompt('Email'))
      .then(handleSuccess,handleError);
    }
    
    $scope.register = function(){
      djangoAuth.register(prompt('Username'),prompt('Password'),prompt('Email'))
      .then(handleSuccess,handleError);
    }
    
    $scope.verify = function(){
      djangoAuth.verify(prompt("Please enter verification code"))
      .then(handleSuccess,handleError);
    }
    
    $scope.goVerify = function(){
      $location.path("/verifyEmail/"+prompt("Please enter verification code"));
    }
    
    $scope.changePassword = function(){
      djangoAuth.changePassword(prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    }
    
    $scope.profile = function(){
      djangoAuth.profile()
      .then(handleSuccess,handleError);
    }
    
    $scope.updateProfile = function(){
      djangoAuth.updateProfile({'first_name': prompt("First Name"), 'last_name': prompt("Last Name"), 'email': prompt("Email")})
      .then(handleSuccess,handleError);
    }
    
    $scope.confirmReset = function(){
      djangoAuth.confirmReset(prompt("Code 1"), prompt("Code 2"), prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    }

    $scope.goConfirmReset = function(){
      $location.path("/passwordResetConfirm/"+prompt("Code 1")+"/"+prompt("Code 2"))
    }
    
    var handleSuccess = function(data){
      $scope.response = data;
    }
    
    var handleError = function(data){
      $scope.response = data;
    }

    $scope.show_login = true;
    $scope.$on("djangoAuth.logged_in", function(data){
      $scope.show_login = false;
    });
    $scope.$on("djangoAuth.logged_out", function(data){
      $scope.show_login = true;
    });

    $scope.posts = [];
    $http.get('/api/posts').then(function(result) {
      angular.forEach(result.data, function(item) {
        $scope.posts.push(item);
      });
    });

    $scope.post_text = '';
  	$scope.complete = false;
    $scope.addPost = function(formData){
      function validatePost(post) {
        var urlRegex = /^(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?$/;
        var hashtagRegex = /^(#[a-z\d][\w-]*)$/;

        console.log(urlRegex.test(post));
        console.log(hashtagRegex.test(post));
        console.log(urlRegex.test(post) || hashtagRegex.test(post));

        return (urlRegex.test(post) || hashtagRegex.test(post));
      }

      $scope.errors = [];
      $scope.error = '';
      if (!validatePost($scope.post_text)) {
        $scope.error = 'Enter the correct url or hashtag';
      }

      Validate.form_validation(formData, $scope.errors);

      if(!formData.$invalid){
        djangoAuth.profile().then(function(data){
          var username = data.username;
          var formPostData = {text: $scope.post_text, author: username};
          $http({
            method: 'POST',
            url: '/api/posts',
            data: formPostData,
            headers: {'Content-Type': 'application/json'}
          })
          .then(function (data) {
            // success case
            $location.path("/");
          }, function (data) {
            // error case
            $scope.errors = data;
          });
        });
      }
    }
  });
