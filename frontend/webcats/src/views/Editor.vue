<template lang="">
  <div class='col-md-12 p-5 pt-3 d-flex align-items-start flex-column'>
    <div class="col-md-12 d-flex flex-row justify-content-between card p-2 mb-1">
      <div class="d-flex flex-row">
        <div class='d-flex flex-column'>
          <h3>Editor</h3>
          <router-link class="" :to="'/'">
            <button class='btn btn-block btn-outline-secondary btn-sm'>&lt;- Back</button>
          </router-link> 
          <div class='d-flex flex-column pt-3'>
            <div> Node ID:   <b>{{ selected_item.id }}</b> </div>
            <div> Node Type: <b>{{ selected_item.type }}</b> </div>
          </div>
        </div>
      </div>
      <div class='d-flex flex-row'>
        <div class="d-flex flex-row">
          <div class="form-group  px-2">
            <label for="input">Height ( px )</label>
            <input type="number" class="form-control" id="input" placeholder="Enter value" min="0" v-model="selected_item.styles.height">
          </div>
          <!-- <div class="form-group">
            <label for="input">ширина ( px )</label>
            <input type="number" class="form-control" id="input" placeholder="Enter value" min="0" v-model="selected_item.styles.width">
          </div> -->
          <div class="form-group px-2">
            <label for="input">Width by grid (1-12)</label>
            <input type="number" class="form-control" id="input" placeholder="Enter value" max="12" min='1' v-model="selected_item.styles.width_grid">
          </div>
          <div class="form-group px-2" v-show="selected_item.type == 'text'">
            <label for="input">Value of item</label>
            <input type="text" class="form-control" id="input" placeholder="Enter value" max="12" min='1' v-model="selected_item.styles.value">
          </div>
          <div class="form-group px-2" v-show="selected_item.type == 'text'">
            <label for="input">Font size</label>
            <input type="number" class="form-control" id="input" placeholder="Enter value" max="12" min='1' v-model="selected_item.styles.font_size">
          </div>
          <div class="form-group px-2">
            <label>Color</label>
            <div class="input-group my-colorpicker2 colorpicker-element" data-colorpicker-id="2">
              <input type="color" class="form-control" style="height: 38px; width: 45px;" data-original-title="" title="" v-model="selected_item.styles.color">
            </div>
          </div>
          <div class="form-group px-2">
            <label>Background</label>
            <div class="input-group my-colorpicker2 colorpicker-element" data-colorpicker-id="2">
              <input type="color" class="form-control" style="height: 38px; width: 45px;" data-original-title="" title="" v-model="selected_item.styles.background_color">
            </div>
          </div>
        </div>
      </div>
      <div class='d-flex flex-row'>
          <div class='d-flex flex-column px-2'>
            <button type="button" class="btn btn-block btn-outline-secondary btn-sm my-1" @click="addCanvas">New canvas</button>
            <button type="button" class="btn btn-block btn-outline-secondary btn-sm my-1" @click="addText">New text</button>
          </div>
          <div class='d-flex flex-column px-2'>
            <button type="button" class="btn btn-block btn-outline-danger btn-sm my-1" @click="deleteItem">Delete item</button>
            <button type="button" class="btn btn-block btn-outline-secondary btn-sm my-1" @click="addImage">Create image</button>
          </div>
        </div>
    </div>
    
    <div class="col-md-12 mt-3">
      <ItemTree class="m-auto" :item_list='canvas' @handle-click="setSelectedtItem" />
    </div>
  </div>
</template>
<script>
import ItemTree from "@/components/ItemTree.vue"
import { ColorPicker } from 'vue-color-kit'
import 'vue-color-kit/dist/vue-color-kit.css'

const base_item = {
    id: 0,
    position:0,
    type: 'canvas',
    active: false,
    deleted: false,
    styles: {
      value: '',
      height: 0,
      width: 0,
      width_grid: 5,
      color: '',
      background_color: '',
      font_size: '',
      classes: ['d-flex align-items-center justify-content-center flex-wrap', 'column']
    },
    item_list:[]
}

var canvas_root = JSON.parse(JSON.stringify(base_item))
canvas_root.type = 'canvas-root'

export default {
  components:{
    ItemTree,
  },
  data() {
    return {
      selected_item: base_item,
      canvas: canvas_root,
      color_code: null,
      colors: [
          {"hex" : "#FFFFFF"}, {"hex" : "#000000"}, {"hex" : "#FF00FF"}, {"hex" : "#FFFF00"}, 
          {"hex" : "#000FFF"}, {"hex" : "#F0F0F0"}, {"hex" : "#0F0F0F"}, {"hex" : "#00FF00"}
      ],
    }
  },
  methods: {
    changeColor(color) {
        const { r, g, b, a } = color.rgba
        this.color = `rgba(${r}, ${g}, ${b}, ${a})`
      },
    openSucker(isOpen) {
      if (isOpen) {
      } else {
      }
    },
    setSelectedtItem(node) {
      this.selected_item.active = !this.selected_item.active
      this.selected_item = node
    },
    addCanvas(){
      var new_item = JSON.parse(JSON.stringify(base_item))
      new_item.active = false
      this.selected_item.item_list.push(new_item)
      if (base_item.item_list.length != 0){
        base_item.item_list.splice(0, 1)
      } 
    },
    addText(){
      var new_item = JSON.parse(JSON.stringify(base_item))
      new_item.active = false
      new_item.styles.value = "New text"
      new_item.type = 'text'
      this.selected_item.item_list.push(new_item)
      if (base_item.item_list.length != 0){
        base_item.item_list.splice(0, 1)
      } 
    },
    addImage(){
      var new_item = JSON.parse(JSON.stringify(base_item))
      new_item.active = false
      new_item.type = 'image'
      this.selected_item.item_list.push(new_item)
      if (base_item.item_list.length != 0){
        base_item.item_list.splice(0, 1)
      } 
    },
    deleteItem(){
      if (this.selected_item.type == "canvas-root"){
        return
      }
      this.selected_item.active = false
      this.selected_item.deleted = true
      console.log(this.selected_item.deleted)
      this.selected_item = base_item
    }
  },
  
  mounted() {
  },
  
}
</script>
<style lang="scss">
  .toolbar{
    // border-bottom: 1px solid;
    width: 100%;
  }
  .workflow{
    border: 1px dashed;
    width: 100%;
    min-height: 100vh;
  }

.item{
  border: 1px dashed;
}
.item-active{
  border: 2px dashed rgb(0, 247, 255);
}
label{
  font-size: 14px;
}
</style>