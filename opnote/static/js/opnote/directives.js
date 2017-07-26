// directives.directive("timeSet", function ($parse) {
//   return {
//     restrict: 'A',
//     scope: true,
//     link: function (scope, element, attrs) {
//       "use strict";
//       var populated = $parse(attrs.timeSet)(scope);
//       if(!populated){
//         scope.internal = {time_field: new Date()};
//       }
//       else{
//         scope.internal = {
//           time_field: moment(populated, 'HH:mm:ss').toDate()
//         };
//       }
//
//       scope.$watch("internal.time_field", function(){
//         var populated = $parse(attrs.timeSet);
//         var asTimeStr = moment(scope.internal.time_field).format("HH:mm:ss");
//         populated.assign(scope, asTimeStr);
//       });
//     }
//   }
// });
