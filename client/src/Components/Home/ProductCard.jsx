import React from 'react';
import { styled } from '@mui/system';
import {Link} from 'react-router-dom'
const CardContainer = styled('div')({
  border: '1px solid #ccc',
  padding: 10,
  margin: 8,
  width: 'calc(50% - 24px)', // Adjust the width based on your design
  boxSizing: 'border-box',
  textAlign: 'left',
  display: 'inline-block',
  verticalAlign: 'top',
  backgroundColor: '#f4f4f4', // Light gray background color
});

const ProductImage = styled('img')({
  width: 144,
  height: 150,
  marginBottom: 10,
  textAlign:"center"
});

const Title = styled('p')({
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  whiteSpace: 'nowrap',
  color: 'black',
});

const Discount = styled('span')({
  color: 'green',
  fontSize: '12.5px',
  marginBottom: 10,
});

const Price = styled('span')({
  fontSize: '14px',
  color: 'black',
  fontWeight: 'bold', // Make the price bold
});

const Pric = styled('span')({
  fontSize: '12px',
  color: 'black',
});

const Pr = styled('span')({
  fontSize: '12.5px',
  marginBottom: 10,
  color: 'black',
});

const ProductCard = ({ title, price, discount, imageUrl, pr,id }) => {
  return (
    <>
    <Link to={`product/${id}`}>
    <CardContainer>
      <ProductImage src={imageUrl} alt={title} />
      <Title>{title}</Title>
      <Discount>{discount}</Discount>
      <Pr><del>{pr}</del></Pr>
      <br/>
      <Price>{price}</Price>
      <br />
      <br />
      <Pric>Free Delivery in 2 Days</Pric>
    </CardContainer>
    </Link>
    </>
  );
};

export default ProductCard;