/**
 * Created by laurim on 27.10.15.
 */
var app = angular.module('myApp',['ngRoute']);

//Setting up routes for partial views
var prefix = "/static/intro/"
app.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl : prefix + 'pages/interests.html',
      controller : 'interestController as interest'
    })
    .when('/speciality',{
      templateUrl : prefix + 'pages/speciality.html',
      controller : 'specialityController as speciality'
    })
    .when('/skills',{
      templateUrl : prefix + 'pages/skills.html',
      controller : 'skillsController as skills'
    })
    .when('/about',{
      templateUrl : prefix + 'pages/about.html',
      controller : 'aboutController as about'
    })
    .when('/cards',{
      templateUrl : prefix + 'pages/cards.html',
      controller : 'cardsController as main'
    })
});

// Controllers

app.controller('appCtrl', function($scope){

});

var interests = [
  {
    name: "IT",
    specialities: [
      {name: 'QA'},
      {
        name: 'Front-end',
        skills: [
          {name:'HTML5', selected: false},
          {name:'CSS', selected: false},
          {name:'Javascript', selected: false},
          {name:'Jquery', selected: false},
          {name:'Bootstrap', selected: false}
        ]
      },
      {name: 'Back-end'},
      {name: 'UI/UX'},
      {name: 'Management'},
      {name: 'Testing'}
    ],
  },
  {
    name: "Marketing"
  },
  {
    name: "BD"
  },
  {
    name: "Design"
  },
  {
    name: "Finance"
  },
  {
    name: "Tourism"
  },
  {
    name: "Service"
  }
];

var findSelected = function(collection, selected) {
  found = null;
  angular.forEach(collection, function(k) {
    if(k.name == selected) found = k;
  }, found);
  return found
};

window.tiitusOnboardingState = {};
app.controller('interestController', function($scope){
  $scope.firstName = window.tiitusUser.first_name;
  this.interests = interests;
  $scope.go = function(e) {
    var link = $(e.target);
    window.tiitusOnboardingState.interest = findSelected(interests, link.data("interest"));
  };
});

app.controller('specialityController', function($scope){
  this.specialities = tiitusOnboardingState.interest.specialities;
  $scope.go = function(e) {
    var link = $(e.target);
    window.tiitusOnboardingState.speciality = findSelected(tiitusOnboardingState.interest.specialities, link.data("speciality"));
  };
});

app.controller('skillsController', function($scope){
  this.skills = window.tiitusOnboardingState.speciality.skills;
  var that = this;

  $scope.toAddSkill = false;

  $scope.addSkill = function(){
    that.skills.push({name: $scope.newSkill, selected: false});
    $scope.toAddSkill = false;
  };

//REFACTOR THIS to a DIRECTIVE!
  $scope.toggleSkill = function(skill){
    if (!this.skill.selected){
      this.skill.selected = true;
    }
    else {
      this.skill.selected = false;
    }
  };
  $scope.confirmSkills = function(){
    selected = []
    that.skills.forEach(function(skill){
      if (skill.selected) {
        selected.push(skill);
      }
    });
    window.tiitusOnboardingState.skills = selected;
  }
});

app.controller('aboutController', ['$scope', '$http', '$location', function($scope, $http, $location){
  $scope.aboutValue = { text: '' };
  $scope.go = function() {
    $scope.loading = true;
    var profile = {
      about: $scope.aboutValue.text,
      interest: tiitusOnboardingState.interest.name,
      speciality: tiitusOnboardingState.speciality.name,
      skills: tiitusOnboardingState.skills.map(function(i) { return i.name }).join(",")
    }
    $.post('/profile/', profile, function(response) {
      $scope.loading = false;
    })
    $location.path('/cards');
  };
}]);

var defaultJobs = [
  {logo:'images/tieto.png', jobTitle:'Full Stack Developer', company:'Tieto', image:'images/developer.jpg', skills:'HTML5/CSS/Mobile-friendly', description: 'Lorem ipsum blaa blaa blaa...', dtn2: 'More about the position at Tieto...'},
  {logo:'images/reaktor.gif', jobTitle:'Front End Developer', company:'Reaktor', image:'images/developer.jpg', skills:'HTML5/CSS/Javascript/React', description: 'Lorem ipsum blaa blaa blaa...', dtn2: 'More about the position at Reaktor...'},
  {logo:'images/futurice.png', jobTitle:'Bad-Ass Developer', company:'Futurice', image:'images/developer.jpg', skills:'Java/HTML5/CSS', description: 'Lorem ipsum blaa blaa blaa...', dtn2: 'More about the position at Futurice...'}
];
app.controller('cardsController', ['$scope', '$http', function($scope, $http){
  init();

  function init() {
    $scope.firstName = window.tiitusUser.first_name;
    $scope.jobs = [];
    $http.get("/positions/").then(function(response) {
console.log(response)
var data = response.data;
      var loaded = data.map(function(p) {
        return {
          id: p.id,
          jobTitle: p.title,
          dtn2: p.details,
          company: p.company_name,
          description: p.description,
          skills: p.requirements,
          logo: '',
          image: '/static/intro/images/developer.jpg',
        };
      });

      $scope.jobs = loaded;
    })
    $scope.job_index = 0;
    $scope.appliedJobs = []; // in reality, it may not be a good idea to put applied jobs in an object array (consider page reload for example), but it works for demo purposes.
    $scope.discardedJobs = []; // same as above...this is just for simplifying the discard-function.
    $scope.showMore = false;

    $scope.discard = function() { //When user clicks next job, move on to next job and remove from object array - in "live version", the cards should be handled immediately to prevent them from a) not being shown b) shown more than once.
      var discarded = $scope.jobs[$scope.job_index];
      $scope.discardedJobs.push(discarded);
      $scope.showMore = false;
      $scope.job_index ++;
      /*animate = function(){
        $("#animate-target").animate({ // this is a jquery animation "template" to be set on any element that needs more interactivity
          opacity: '0'
        },100);
      }
      animate();*/
    };

    $scope.apply = function(){ //When user clicks apply, the currently displayed job is pushed from "jobs" to "applied jobs". In reality again, see above comment.
     console.log($scope.jobs[$scope.job_index]) 
      $.post("/apply/?id=" + $scope.jobs[$scope.job_index].id)
      var applied = $scope.jobs[$scope.job_index];
      $scope.appliedJobs.push(applied);
      $scope.job_index ++;
    };

    $scope.learnMore = function(){ //When user clicks "learn more", hidden element with more information about the job is shown
      if (!$scope.showMore) {
        $scope.showMore = true;
      }
      else {$scope.showMore = false}
    };
  };
}]);

