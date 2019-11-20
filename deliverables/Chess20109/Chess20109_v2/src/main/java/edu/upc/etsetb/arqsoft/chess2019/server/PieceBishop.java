/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

import java.util.ArrayList;

/**
 *
 * @author jordi
 */
public class PieceBishop extends Piece {
    
    public PieceBishop(String figure, Color color) {
        super(figure, color);
    }
    
    @Override
    public boolean isPieceMovement(int rO, int cO, int rD, int cD) throws NoPieceMovementException
    {
        boolean valid = false;
        int variationC,variationR;
        variationC = Math.abs(cO - cD);
        variationR = Math.abs(rO - rD);
        
        return variationC == variationR;
    }
    
    @Override
    public boolean isPathFree(int rO, int cO, int rD, int cD, Board board) throws NoPathFreeException
    {
        boolean isFree = false;
        int distanceX = cD - cO;
        int distanceY = rD - cD;
        int count = 0;
        int positionX = cO;
        int positionY = rO;
        ArrayList<Integer> coordinates;
        while(positionX<cD && positionY<rD){
            positionY ++;
            positionX ++;
            coordinates  = new ArrayList<Integer>();
            coordinates.add(positionX);
            coordinates.add(positionY);
            Piece piece = board.getSquare(coordinates).getPiece();
            if(piece!=null){
                return false;
            }
        }
        return true;
    }
}
