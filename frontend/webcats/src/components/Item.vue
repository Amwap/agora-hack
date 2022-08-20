<template lang="">
    <div 
        v-if="!node.deleted"
        @click.stop="handleClick(node)"
        class="p-2 item " 
        :class="appendClasses"
        v-bind:style="appendStyles"
        > 
        <div class="text" v-show="node.type == 'text'">{{node.styles.value}}</div>
        <div class="image" v-show="node.type == 'image'">
            <img src="" alt="">
        </div>
        <slot></slot>
    </div>
</template>
<script>

export default {
    data() {
        return {
            classes:[ ],
            styles: { }
        }
    },
    props:{
        handleClick: Function,
        selected_item: Object
    },
    computed:{
        appendClasses(){
            this.classes = [
                `col-md-${this.node.styles.width_grid}`,
                ...this.node.styles.classes
            ]
            this.defineClass(this.node.active, 'item-active')
            return this.classes
        },
        appendStyles(){
            this.styles = {
                height: `${this.node.styles.height}px`,
                color: this.node.styles.color,
                'background-color': this.node.styles.background_color
                'font-size': this.node.styles.font_size
                // width: `${this.node.styles.width}px`
            }
            if (this.node.styles.height == 0){ this.styles.height = 'auto' }
            // if (this.node.styles.width == 0){ this.styles.width = 'auto' }
            return this.styles
        }
    },
    props:{
        node: Object
    },
    methods: {
        handleClick (node) {
            this.$emit('handle-click', node);
        },
        defineClass(condition, item_class){
            if (condition){
                this.classes.push(item_class)
            }else{
                var index = this.classes.indexOf(item_class);
                if (index !== -1) { this.classes.splice(index, 1); }
            }
        }
    },
}
</script>
<style lang="scss" scoped>
.item{
  border: 1px dashed black!important;
}
.item-active{
  border: 2px dashed rgb(0, 247, 255)!important;
}
</style>