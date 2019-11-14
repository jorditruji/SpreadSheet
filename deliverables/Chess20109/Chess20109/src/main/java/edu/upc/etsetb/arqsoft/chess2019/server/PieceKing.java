/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

/**
 *
 * @author jordi
 */
public class PieceKing extends Piece {

    public PieceKing(String figure, Color color) {
        super(figure, color);
    }
    
    @Override
    public boolean isPieceMovement(int rO, int cO, int rD, int cD) throws Piece.NoPieceMovementException
    {
        boolean valid = false;
        int variationC,variationR;
        variationC = cO - cD;
        variationR = rO - rD;
        
        return variationC == variationR;
    }
}
