<template>
	<div class="testdrive">
		<div class="container">
			<div class="heading">Testdrives Booked</div>
			<b-table
				striped
				class="border-top"
				:items="items"
				:fields="fields"
			></b-table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Testdrives',
	data() {
		return {
			fields: [
				{
					key: 'testdrive_id',
					label: 'Testdrive ID',
					class: 'text-center',
				},
				{
					key: 'model_id',
					label: 'Model ID',
					class: 'text-center',
				},
				{
					key: 'testdrive_date',
					label: 'Testdrive Date',
					class: 'text-center',
				},
				{
					key: 'state',
					label: 'State',
					class: 'text-center',
				},
				{
					key: 'city',
					label: 'City',
					class: 'text-center',
				},
				{
					key: 'comments',
					label: 'Comments',
					thStyle: 'width: 40%; text-align: center;',
				},
			],
			items: [],
		};
	},
	methods: {
		async loadCustTestdrives() {
			await axios
				.get(`http://localhost:5000/testdrives/${this.$route.params.cust_id}`)
				.then((response) => {
					this.items = response.data;
				});
		},
	},
	mounted() {
		this.loadCustTestdrives();
	},
};
</script>

<style scoped>
.testdrive {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 50px;
}
</style>
