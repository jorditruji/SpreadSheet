/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

import java.util.ArrayList;

/**
 *
 * @author JuanCarlos
 */
public class Game {

    private ServerProtocolMngr protMngr;

    protected ArrayList<Player> players;
    protected Board board;
    protected Color turn;

//    

    public Game() {
        this.players = new  ArrayList<Player>();
        this.board = new Board();
        this.turn =  Color.WHITE;
        Player player;
        for (Color color : Color.values()) { 
            player = new Player(color, this.board);
            this.players.add(player);
            
        }
  

    }

    public Color getTurn() {
        return turn;
    }

    public void setTurn(Color turn) {
        this.turn = turn;
    }

    public ArrayList<Player> getPlayers() {
        return this.players;
    }
    
    public Player getActualPlayer(Color color){
        for(Player player: this.getPlayers()){
            if (player.getColor().equals(color)){
                return player;
            }
        }
        return null;
    }

    public void setPlayers(ArrayList<Player> players) {
        this.players = players;
    }

    public Board getBoard() {
        return board;
    }

    public void setBoard(Board board) {
        this.board = board;
    }

    public void setServerProtMngr(ServerProtocolMngr protMngr) {
        this.protMngr = protMngr;
    }

    public void move(int rO, int cO, int rD, int cD) {
        /*
        Initial version: it just sends back an OK message to the client.
        You should modify its code for implementing the sequence diagram in the 
        script of the lab session

        NOTE: USE THE FOLLOWING UNCOMMENTED INSTRUCTION FOR SENDING AN ERROR MESSAGE TO THE CLIENT.
        AN ERROR MESSAGE SHALL BE AN END-OF-LINE FREE STRING STARTING WITH "E "
         */
        //         this.protMngr.sendFromServerToClient("E this is an error message");
        // Check if there was actually a piece in the position

        Piece pieceOrigen = this.getPiece(rO, cO);
        if (pieceOrigen == null){
            this.protMngr.sendFromServerToClient("E Square is empty. No piece to move");
            return;
        }
        
        //CHECK THE PIECE BELONGS TO THE PLAYER WHO IS MOVING
        if (!pieceOrigen.getColor().equals(this.turn)){
            this.protMngr.sendFromServerToClient("E Requested piece does not belong to you. Please do not cheat.");
            return;           
        }
        
        //CHECK FOR DESTINATION SQUARE
        Piece pieceDestino = this.getPiece(rD, rD);
        
        //CHECK IF THE SQUARE DESTINY IS EMPTY
        if(pieceDestino != null){
            if (pieceDestino.getColor().equals(this.turn)){
                this.protMngr.sendFromServerToClient("E Destination square is already occupied by one of your pieces");
                return;   
            }
        }

        Player actualPlayer = this.getActualPlayer(this.turn);
        String message = actualPlayer.move(pieceOrigen, rO, cO, rD, cD, board);
        if(!message.isEmpty()){
            this.protMngr.sendFromServerToClient(message);
        }
        //Proceed to move
        
        /* 
        DO NOT CHANGE THE CODE BELOW.
        FINAL PART OF THE METHOD. IF ARRIVED HERE, THE MOVEMENT CAN BE PERFORMED
        METHOD assessCheckOrCheckMate(...) CHECKS WHETHER THERE IS CHECK OR CHECK-MATE.
        IF IT IS CHECK-MATE THE METHOD RETURNS TRUE AND A NON-EMPTY STRING
        IF THERE IS CHECK THE METHOD RETURNS FALSE AND A NON-EMPTY STRING
        IF THERE IS NONE OF BOTH, THE METHOD RETURNS FALSE AND AN EMPTY STRING
         */
        StringBuilder assessMess = new StringBuilder();
        boolean isCheckMate = this.assessCheckOrCheckMate(assessMess);

        if (assessMess.length() == 0) {
            this.protMngr.sendFromServerToClient("OK");
        } else {
            this.protMngr.sendFromServerToClient(assessMess.insert(0, "OK\n").toString());
        }
        if(isCheckMate){
            this.proceedToFinalizedGame() ;
        }

    }

    private boolean assessCheckOrCheckMate(StringBuilder assessMess) {
        // IF THE PROGRAM SHOULD BE COMPLETED, IT SHOULD BE IMPLEMENTED
        return false ;
    }

    private void proceedToFinalizedGame() {
        // IF THE PROGRAM SHOULD BE COMPLETED, IT SHOULD BE IMPLEMENTED
        return ;
    }
    
    private Piece getPiece(int r0, int c0) {
        ArrayList<Integer> position = new ArrayList<Integer>();
        position.add(c0);
        position.add(r0);
        
        Piece piece = this.board.getSquare(position).getPiece();
        return piece;
    }
}
