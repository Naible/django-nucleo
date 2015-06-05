'use strict';

angular.module('angularDjangoRegistrationAuthApp')
  .controller('UserprofileCtrl', function ($scope, $http, djangoAuth, Validate) {
    $scope.model = {'first_name':'','last_name':'','email':''};
    $scope.posts = [];
  	$scope.complete = false;

  	djangoAuth.profile().then(function(data){
      var username = data.username;
  		var url = 'api/users/' + username + '/posts';
      $http.get(url).then(function(result) {
        angular.forEach(result.data, function(item) {
          $scope.posts.push(item);
        });
      });
      $scope.model = data;
  	});
    $scope.updateProfile = function(formData, model){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.updateProfile(model)
        .then(function(data){
        	// success case
        	$scope.complete = true;
        },function(data){
        	// error case
        	$scope.error = data;
        });
      }
    }
  });
