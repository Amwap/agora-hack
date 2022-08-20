<template lang="">
    <ItemNode :node="item_list" :handle-click="handleClick" ></ItemNode>
</template>
<script>
import ItemNode from "./ItemNode.vue";
export default {
    
    props: {
        item_list: Object,
        // selected_item: Object
        // handleClick: Function
    },
    components: {
        ItemNode
    },
    methods: {
        handleClick (node) {
                this.$emit('node-click', node);
            }
    },
}
</script>
<style lang="">
    
</style>