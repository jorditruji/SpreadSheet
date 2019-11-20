/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author jordi
 */
public class PieceBishopTest {
     private PieceBishop bishop;// = new PieceBishop(figure,black );
    public PieceBishopTest() {
        Color black = Color.BLACK;
        String figure = "W";
        this.bishop = new PieceBishop(figure,black );
    }
    
    @BeforeClass
    public static void setUpClass() {
        System.out.println("*****************************************\n");
        System.out.println("Testing class PieceBishop\n ");
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }
    /**
     * Test constructor of  class PieceBishop and get color.
     */
    @Test
    public void testConstructorAndGetColor() throws Exception {

        assertEquals( Color.BLACK, this.bishop.getColor());
    }
    
    /**
     * Test of isPieceMovement method, of class PieceBishop.
     */
    @Test
    public void testIsPieceMovement() throws Exception {
        System.out.println("isPieceMovement");
        int rO = 0;
        int cO = 0;
        int rD = 0;
        int cD = 0;
        PieceBishop instance = null;
        boolean expResult = false;
        boolean result = instance.isPieceMovement(rO, cO, rD, cD);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of isPathFree method, of class PieceBishop.
     */
    @Test
    public void testIsPathFree() throws Exception {
        System.out.println("isPathFree");
        int rO = 0;
        int cO = 0;
        int rD = 0;
        int cD = 0;
        Board board = null;
        PieceBishop instance = null;
        boolean expResult = false;
        boolean result = instance.isPathFree(rO, cO, rD, cD, board);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
