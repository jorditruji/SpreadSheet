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
public class PiecePawn extends Piece{

    public PiecePawn(String figure, Color color) {
        super(figure, color);
    }
    @Override
    public boolean isPieceMovement(int rO, int cO, int rD, int cD) throws NoPieceMovementException
    {
        return false;
    }

    @Override
    public boolean isPathFree(int rO, int cO, int rD, int cD, Board board) throws NoPathFreeException {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
