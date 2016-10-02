var clientResources = angular.module('clientResources', []);

clientResources.factory('Categories',function($resource){
        return $resource('/categories/:id ',{id:'@id'}
        ,{
                update:{
                        method:'PUT'
                }
        }

        );
});


