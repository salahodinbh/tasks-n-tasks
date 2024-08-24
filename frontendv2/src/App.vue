<template>
  <div>
    <!-- <h1>{{ message }}</h1> -->
    <LoadingInit/>
    <!-- Supposedly I can create css classes with the name "fade" and play with the transition, but for some reason it doesn't work -->
    <transition name="fade" @before-enter="beforeEnter" @enter="enter">  
    <div class="fade" v-if="!loading">
        <div>
          <h1 class="flex flex-col items-center">To-Do List POC</h1>
            <div class="flex flex-row">
            <div v-for="(task, index) in tasks" :key="index" class="flex items-center mb-2">
              <p>{{ task }}</p>
              <CommonButton text="Remove" @click="removeTask(index)" />
              <CommonButton text="Complete" @click="completeTask(index)" />
            </div>
            <div v-for="(completedTask, index) in completedTasks" :key="index" class="flex items-center mb-2">
              <p>{{ completedTask }}</p>
            </div>
          </div>
          <div class="flex items-center">
            <input v-model="newTask" @keydown.enter="addTask" placeholder="Add a new task" />
            <CommonButton text="Add" @click="addTask" />
          </div>
        </div>  
      <router-view />
    </div>
  </Transition>
  </div>
</template>

<script>
import CommonButton from './components/CommonButton.vue';
import LoadingInit from './components/LoadingInit.vue';

export default {

  data() {
    return {
      //message: ""
      tasks: [],
      completedTasks: [],
      newTask: "",
      loading: true
    };
  },
  mounted() {
    /**fetch("http://localhost:5000/")
      .then((response) => response.text())
      .then((data) => {
        this.message = data;
      });
      */
    this.fetchTasks();
    setTimeout(() => {
      this.loading = false;
    }, 2000);
  },
  methods: {
    addTask() {
      if (this.newTask.trim() !== "") {
        fetch("http://localhost:5000/tasks", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ task: this.newTask })
        })
          .then(() => {
            this.fetchTasks();
            this.newTask = "";
          });
      }
    },
    completeTask(index) {
      fetch(`http://localhost:5000/tasks/${index}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({index})
      })
        .then(() => {
          this.fetchTasks();
          this.fetchCompletedTasks();
        });
    },
    removeTask(index) {
      fetch(`http://localhost:5000/tasks/${index}`, {
        method: "DELETE"
      })
        .then(() => {
          this.fetchTasks();
        })
    },
    fetchTasks() {
      fetch("http://localhost:5000/tasks")
        .then((response) => response.json())
        .then((data) => {
          this.tasks = data;
        });
    },
    fetchCompletedTasks() {
      fetch("http://localhost:5000/completedtasks")
        .then((response) => response.json())
        .then((data) => {
          this.completedTasks = data;
        });
    },
    beforeEnter(el) {
      el.style.opacity = 0;
    },
    enter(el, done) {
      el.offsetHeight; 
      el.style.transition = 'opacity 1s';
      el.style.opacity = 1;
      done();
    }
  },
  components: {
    CommonButton,
    LoadingInit,
  }
};
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
}
</style>