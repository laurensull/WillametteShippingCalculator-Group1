#!/usr/bin/python3

################################
# File Name:	test_ShippingLogicUnitTest.py
# Author:		Lauren Sullivan
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for Shipping Logic
################################


import unittest
from ShippingLogic import ShippingLogic
from ShippingLogic import SaleShippingLogic
from basket import Basket
from SaleItem import SaleItem

class TestShippingLogic(unittest.TestCase):
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theShippingLogic = ShippingLogic()
		self.theSaleShippingLogic = SaleShippingLogic()
		self.basket1 = Basket()
		self.basket2 = Basket()
		self.saleItem = SaleItem(['20', '1', "Sweater"])
		self.freeShippingItem = SaleItem(['20', '1', "SweaterFreeShipping", 'FS'])
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do
	
	def test_CalcWeightForCost(self):
		
		self.basket1.addItem(1, self.saleItem)
		costWithFirstItem = self.theShippingLogic.calcWeightForCost()
		
		self.assertEqual(costWithFirstItem, 20)
		
		self.basket1.addItem(1, self.freeShippingItem)
		costWithSecondItem = self.theShippingLogic.calcWeightForCost()
		
		#cost should be the same since free shipping for second item
		self.assertEqual(costWithSecondItem, costWithFirstItem )
		
		self.assertEqual(self.freeShippingItem.getFreeShipping(), True)
		
		
	def test_calcCostForShippingByWeight(self):
		
		self.assertEqual(self.theShippingLogic.calcCostForShippingByWeight( saleItem.getWeight()), 20)
		
		self.assertEqual(self.theShippingLogic.calcCostForShippingByWeight(freeShippingItem.getWeight()), 0)
		
		
	def test_CalcWeightForCostWithSaleShipping (self):
		
		self.basket2.addItem(1, self.saleItem)
		costWithFirstItem = self.theSaleShippingLogic.calcWeightForCost()
		
		self.assertEqual(costFirstItem, 20)
		
		self.basket2.addItem(1, self.freeShippingItem)
		costWithSecondItem = self.theShippingLogic.calcWeightForCost()
		
		#cost should be the same since free shipping for second item
		self.assertEqual(costWithSecondItem, costWithFirstItem )
		
	def test_calcCostForShippingByWeightForSaleShipping(self):
		
		self.assertEqual(self.theSaleShippingLogic.calcCostForShippingByWeight( saleItem.getWeight()), 5)
		
		self.assertEqual(self.theSaleShippingLogic.calcCostForShippingByWeight(freeShippingItem.getWeight()), 5)
