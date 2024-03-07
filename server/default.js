import Product from './model/productSchema.js';
import { products } from './constants/product.js';

const DefaultData = async () => {
    try {
        // Assuming 'products' is a Mongoose model
        await Product.deleteMany();
        await Product.insertMany(products); // Assuming 'products' is an array of data

        console.log('Data imported successfully');
        
    } catch (error) {
        console.log('Error: ', error.message);
    }
}

export default DefaultData;
