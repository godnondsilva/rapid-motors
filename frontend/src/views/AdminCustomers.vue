<template>
	<div class="customers">
		<div class="container">
			<div class="heading">All customers</div>
			<b-table
				class="border-top"
				striped
				:items="items"
				:fields="fields"
			></b-table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Customers',
	data() {
		return {
			fields: [
				{
					key: 'cust_id',
					label: 'Customer ID',
					class: 'text-center',
				},
				{
					key: 'name',
					label: 'Name',
				},
				{
					key: 'email',
					label: 'Email',
				},
				{
					key: 'phone',
					label: 'Phone',
				},
				{
					key: 'address',
					label: 'Address',
					thStyle: 'width: 30%;',
				},
			],
			items: [],
		};
	},
	methods: {
		async loadAdminCustomers() {
			await axios
				.get('http://localhost:5000/admincustomers')
				.then((response) => {
					this.items = response.data;
				});
		},
	},
	mounted() {
		this.loadAdminCustomers();
	},
};
</script>

<style scoped>
.customers {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 50px;
}
</style>
