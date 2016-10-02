BlogApp.controller('FirstPageCtrl',function($scope,$http,Categories){
     $scope.pageTitle= 'Test';
     var category = Categories.get({id:5}, function() {
          category.title = 'testForDelete';
          category.$update();
          category.$delete();
     });

    var cat = {'title':'new537'};
    Categories.save(cat);
 });
