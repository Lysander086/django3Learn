const app = new Vue({
  el: '#app',
  data: {}
})


Vue.component("todo", {
  props: ['tasks', 'remaining'],
  template:
      `
    <div class="todo-main">
      <p><strong>Remaining Tasks: {{remaining}} </strong></p>
      
    </div>
  `,
  data() {
    return {

    }
  }
})
