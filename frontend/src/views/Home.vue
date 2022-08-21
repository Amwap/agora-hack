<template lang="">
  <div class='col-md-12 p-5 pt-3 d-flex align-items-start flex-column'>
    <h3>Projects</h3>
    <div class="col-md-12 row">
      <router-link class="project-card card p-3 m-3" :to="'/editor/new'">
        <div class="col-md-12">
          <h6>New project</h6>
          <div class=""></div>
          <div class=""></div>
        </div>
      </router-link> 
      <router-link class="project-card  card p-3 m-3" :to="'/editor/' + project.id"  v-for="project in project_list">
        <div class="col-md-12">
          <h6>{{ project.title }}</h6>
          <div class="">Created at: {{ project.created_at }}</div>
          <div class="">Last edit: {{ project.last_edit }}</div>
        </div>
      </router-link> 
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from 'axios'

var project_list = []
export default {
  data() {
    return {
      project_list: []
    }
  },
  methods:{
    getData(){
      axios.request({
        method: 'get',
        url: `${import.meta.env.VITE_API_URL}api/v1/editor/get/project_list/`,
        // data: base_item,
        })
      .then((response) => {
        this.project_list = response.data
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },
  mounted() {
    this.getData()
  },
  
}
</script>

<style lang="scss" scoped>
.project-card{
  width: 250px;
  text-decoration: none;
  color: #666;
}
.project-card:hover{
  box-shadow: 0px 0px 5px black;
  transition: 0.2s;
  user-select: none;
  
}
.project-card:hover{
  transition: 0.2s;
}
  
</style>