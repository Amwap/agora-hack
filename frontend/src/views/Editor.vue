<template lang="">
    <!-- <Crutch :class="{'d-block': show_preview, 'd-none': show_preview}" @hidePreview="show_preview=false" :canvas="show_preview=true"/> -->

<nav class="navbar navbar-light bg-light">
  <router-link class="" :to="'/'">
      <button class="btn btn-block btn-outline-secondary btn-sm">
        <img src="https://img.icons8.com/ios-glyphs/30/5B6A6D/circled-menu.png"/>
      </button>
    </router-link>
  <a class="navbar-brand" href="#">
  </a>
</nav>
  <div class="col-md-12 p-5 pt-3 d-flex align-items-start flex-column">
    <div class="col-md-12 d-flex flex-row justify-content-between card p-2 mb-1">
      <div class="d-flex flex-row">
        <div class="d-flex flex-column">
          <h3>Editor</h3>          
          <div class="d-flex flex-column pt-3">
            <div>
              Project ID: <b>{{ getProjectId }}</b>
            </div>
            <div>
              Node ID: <b>{{ selected_item.id }}</b>
            </div>
            <div>
              Node Type: <b>{{ selected_item.type }}</b>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex flex-row">
        <div class="d-flex flex-row">
          <div class="form-group px-2">
            <label for="input">Height (px)</label>
            <input
              type="number"
              class="form-control"
              id="input"
              placeholder="Enter value"
              max="2000"
              min="1"
              v-model="selected_item.styles.height"
            />
          </div>
          <div class="form-group px-2">
            <label for="input">Width by grid (1-12)</label>
            <input
              type="number"
              class="form-control"
              id="input"
              placeholder="Enter value"
              max="12"
              min="1"
              v-model="selected_item.styles.width_grid"
            />
          </div>
          <div class="form-group px-2" v-show="selected_item.type == 'text'">
            <label for="input">Value of item</label>
            <input
              type="text"
              class="form-control"
              id="input"
              placeholder="Enter value"
              max="12"
              min="1"
              v-model="selected_item.styles.value"
            />
          </div>
          <div class="form-group px-2" v-show="selected_item.type == 'text'">
            <label for="input">Font size</label>
            <input
              type="number"
              class="form-control"
              id="input"
              placeholder="Enter value"
              min="1"
              v-model="selected_item.styles.font_size"
            />
          </div>
          <div class="form-group px-2" v-show="selected_item.type != 'text'">
            <label for="input">Border radius</label>
            <input
              type="number"
              class="form-control"
              id="input"
              placeholder="Enter value"
              min="0"
              v-model="selected_item.styles.border_radius"
            />
          </div>
          <div class="form-group px-2">
            <label>Font color</label>
            <div
              class="input-group my-colorpicker2 colorpicker-element"
              data-colorpicker-id="2"
            >
              <input
                type="color"
                class="form-control"
                style="height: 38px; width: 45px"
                data-original-title=""
                title=""
                v-model="selected_item.styles.color"
              />
            </div>
          </div>
          <div class="form-group px-2">
            <label>Background</label>
            <div
              class="input-group my-colorpicker2 colorpicker-element"
              data-colorpicker-id="2"
            >
              <input
                type="color"
                class="form-control"
                style="height: 38px; width: 45px"
                data-original-title=""
                title=""
                v-model="selected_item.styles.background_color"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex flex-row">
        <div class="d-flex flex-column px-2">
          <button
            type="button"
            class="btn btn-block btn-outline-secondary btn-sm my-1"
            @click="addCanvas"
          >
            New canvas
          </button>
          <button
            type="button"
            class="btn btn-block btn-outline-secondary btn-sm my-1"
            @click="addText"
          >
            New text
          </button>
        </div>
        <div class="d-flex flex-column px-2">
          <button
            type="button"
            class="btn btn-block btn-outline-danger btn-sm my-1"
            @click="deleteItem"
          >
            Delete item
          </button>
          <button
            type="button"
            class="btn btn-block btn-outline-secondary btn-sm my-1"
            @click="addImage"
          >
            Create image
          </button>
          <button
            type="button"
            class="btn btn-block btn-warning btn-sm my-1"
            @click="addImage"
            
          >
            Preview
          </button>
        </div>
        
      </div>
    </div>

    <div class="col-md-12 mt-3">
      <ItemTree
        class="m-auto"
        :item_list="canvas"
        @handle-click="setSelectedtItem"
      />
    </div>
  </div>
  
</template>
<script>
import ItemTree from "@/components/ItemTree.vue";
import Crutch from "@/components/Crutch.vue";
import axios from 'axios'
const base_item = {
  id: Date.now(),
  type: "canvas",
  active: false,
  deleted: false,
  parent: null,
  styles: {
    value: "",
    height: 0,
    width: 0,
    width_grid: 5,
    color: "",
    background_color: "",
    font_size: 15,
    border_radius: 0,
    url: "",
    classes: [
      "d-flex align-items-center justify-content-center flex-wrap",
      "column",
    ],
  },
  item_list: [],
};

var canvas_root = JSON.parse(JSON.stringify(base_item));
canvas_root.type = "canvas-root";

export default {
  components: {
    ItemTree,
    Crutch
  },
  data() {
    return {
      project_id: JSON.parse(localStorage.getItem('project_id')),
      selected_item: base_item,
      canvas: canvas_root,
      show_preview: false,
      color_code: null,
      colors: [
        { hex: "#FFFFFF" },
        { hex: "#000000" },
        { hex: "#FF00FF" },
        { hex: "#FFFF00" },
        { hex: "#000FFF" },
        { hex: "#F0F0F0" },
        { hex: "#0F0F0F" },
        { hex: "#00FF00" },
      ],
    };
  },
  computed:{
    getProjectId(){
      return JSON.parse(localStorage.getItem('project_id')) 
    }
  },
  methods: {
    changeColor(color) {
      const { r, g, b, a } = color.rgba;
      this.color = `rgba(${r}, ${g}, ${b}, ${a})`;
    },
    openSucker(isOpen) {
      if (isOpen) {
      } else {
      }
    },
    setSelectedtItem(node) {
      this.selected_item.active = !this.selected_item.active;
      this.selected_item = node;
    },
    
    createNewItem(){
      var new_item = JSON.parse(JSON.stringify(base_item));
      new_item.id = Date.now()
      new_item.parent = this.selected_item.id
      new_item.active = false;
      return new_item
    },
    addCanvas() {
      var new_item = this.createNewItem()
      this.selected_item.item_list.push(new_item);
      if (base_item.item_list.length != 0) {
        base_item.item_list.splice(0, 1);
      }
      this.saveItemData(new_item)
    },
    addText() {
      var new_item = this.createNewItem()
      new_item.styles.value = "New text";
      new_item.type = "text";
      this.selected_item.item_list.push(new_item);
      if (base_item.item_list.length != 0) {
        base_item.item_list.splice(0, 1);
      }
      this.saveItemData(new_item)
    },
    addImage() {
      var new_item = this.createNewItem()
      new_item.type = "image";
      this.selected_item.item_list.push(new_item);
      if (base_item.item_list.length != 0) {
        base_item.item_list.splice(0, 1);
      }
      this.saveItemData(new_item)
    },
    saveItemData(new_item){
      axios.request({
          method: 'post',
          url: `${import.meta.env.VITE_API_URL}api/v1/editor/item/`,
          data: new_item,
          })
        .then((response) => {
            console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    updateItemData(){
      axios.request({
          method: 'update',
          url: `${import.meta.env.VITE_API_URL}api/v1/editor/item/`,
          data: this.selected_item,
          })
        .then((response) => {
            console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteItem() {
      if (this.selected_item.type == "canvas-root") {
        return;
      }
      this.selected_item.active = false;
      this.selected_item.deleted = true;
      console.log(this.selected_item.deleted);
      this.selected_item = base_item;

      axios.request({
          method: 'delete',
          url: `${import.meta.env.VITE_API_URL}api/v1/editor/item/`,
          data: this.selected_item,
          })
        .then((response) => {
            console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },

  mounted(){
    var project_id = window.location.href.split('/').slice(-1)[0]
    if (project_id == 'new'){
        axios.request({
          method: 'post',
          url: `${import.meta.env.VITE_API_URL}api/v1/editor/create/project/`,
          data: base_item,
          })
        .then((response) => {
            this.project_id = response.data.project_id
            this.selected_item.id = response.data.root_id
            this.$router.push({name: 'editor', params: { project_id: this.project_id } })
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    else if (project_id != 'new'){
        this.project_id
        axios.request({
          method: 'get',
          url: `${import.meta.env.VITE_API_URL}api/v1/editor/get/layout/${project_id}`,
          data: base_item,
          })
        .then((response) => {
            this.project_id = response.data.project_id
        })
        .catch(function (error) {
          console.log(error);
        });
      }
  },
};
</script>
<style lang="scss" scoped>
.toolbar {
  // border-bottom: 1px solid;
  width: 100%;
}
.workflow {
  border: 1px dashed;
  width: 100%;
  min-height: 100vh;
}

.item {
  border: 1px dashed;
}
.item-active {
  border: 2px dashed rgb(0, 247, 255);
}
label {
  font-size: 14px;
}
</style>
