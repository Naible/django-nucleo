'use strict';

angular.module('angularDjangoRegistrationAuthApp')
  .controller('MainCtrl', function ($scope, $cookies, $location, djangoAuth, $http, Validate, $route) {
    
    $scope.login = function(){
      djangoAuth.login(prompt('Username'),prompt('password'))
      .then(function(data){
        handleSuccess(data);
      },handleError);
    };
    
    $scope.logout = function(){
      djangoAuth.logout()
      .then(handleSuccess,handleError);
    };
    
    $scope.resetPassword = function(){
      djangoAuth.resetPassword(prompt('Email'))
      .then(handleSuccess,handleError);
    };
    
    $scope.register = function(){
      djangoAuth.register(prompt('Username'),prompt('Password'),prompt('Email'))
      .then(handleSuccess,handleError);
    };
    
    $scope.verify = function(){
      djangoAuth.verify(prompt("Please enter verification code"))
      .then(handleSuccess,handleError);
    };
    
    $scope.goVerify = function(){
      $location.path("/verifyEmail/"+prompt("Please enter verification code"));
    };

    $scope.changePassword = function(){
      djangoAuth.changePassword(prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    };
    
    $scope.profile = function(){
      djangoAuth.profile()
      .then(handleSuccess,handleError);
    };
    
    $scope.updateProfile = function(){
      djangoAuth.updateProfile({'first_name': prompt("First Name"), 'last_name': prompt("Last Name"), 'email': prompt("Email")})
      .then(handleSuccess,handleError);
    };
    
    $scope.confirmReset = function(){
      djangoAuth.confirmReset(prompt("Code 1"), prompt("Code 2"), prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    };

    $scope.goConfirmReset = function(){
      $location.path("/passwordResetConfirm/"+prompt("Code 1")+"/"+prompt("Code 2"))
    };
    
    var handleSuccess = function(data){
      $scope.response = data;
    };
    
    var handleError = function(data){
      $scope.response = data;
    };

    $scope.show_login = true;
    $scope.$on("djangoAuth.logged_in", function(){
      $scope.show_login = false;
    });
    $scope.$on("djangoAuth.logged_out", function(){
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

        return (urlRegex.test(post) || hashtagRegex.test(post));
      }

      $scope.errors = [];
      $scope.error = '';
      var postIsValid = true;
      if (!validatePost($scope.post_text)) {
        $scope.error = 'Enter the correct url or hashtag';
        postIsValid = false;
      }

      Validate.form_validation(formData, $scope.errors);

      if(!formData.$invalid && postIsValid){
        var formPostData = {text: $scope.post_text};
        $http({
          method: 'POST',
          url: '/api/add_post',
          data: formPostData,
          headers: {'Content-Type': 'application/json'}
        })
        .then(function () {
          // success case
          $route.reload();
        }, function (data) {
          // error case
          $scope.errors = data;
        });
      }
    };

    $scope.followUser = function(username) {
      var formPostData = {follows: username};

      $http({
        method: 'POST',
        url: '/api/follow',
        data: formPostData,
        headers: {'Content-Type': 'application/json'}
      })
      .then(function () {
        // success case
        $route.reload();
      }, function (data) {
        // error case
        $scope.errors = data;
      });
    };

    $scope.unfollowUser = function(username) {
      var formPostData = {unfollow: username};

      $http({
        method: 'POST',
        url: '/api/unfollow',
        data: formPostData,
        headers: {'Content-Type': 'application/json'}
      })
      .then(function () {
        // success case
        $route.reload();
      }, function (data) {
        // error case
        $scope.errors = data;
      });
    };

    $scope.caption = 'Following';

    $scope.followingNames = [];
    $http.post('/api/following', [])
    .success(function (data) {
      for (var i=0; i < data.length; i++) {
        $scope.followingNames.push(data[i]);
        console.log(data[i]);
      }
    })
  });