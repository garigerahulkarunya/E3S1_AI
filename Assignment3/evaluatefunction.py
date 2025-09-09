    def evaluate(self):
      
        if self.board.is_checkmate():

            return -10000 if self.player else 10000

        if self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.can_claim_draw():
            return 0

        # Heuristic components

        score = 0.0

        values = {
            chess.PAWN: 1.0,
            chess.KNIGHT: 3.0,
            chess.BISHOP: 3.0,
            chess.ROOK: 5.0,
            chess.QUEEN: 9.0,
            chess.KING: 0.0  
        }

        for sq, piece in self.board.piece_map().items():
            val = values.get(piece.piece_type, 0.0)
        
            if piece.color == chess.WHITE:
                score += val
            else:
                score -= val

        center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
        for csq in center_squares:
            p = self.board.piece_at(csq)
            if p:
                if p.color == chess.WHITE:
                    score += 0.25
                else:
                    score -= 0.25

      
        bcopy = self.board.copy()
  
        bcopy.turn = chess.WHITE
        white_moves = len(list(bcopy.legal_moves))
 
        bcopy.turn = chess.BLACK
        black_moves = len(list(bcopy.legal_moves))
        mobility_value = 0.05 * (white_moves - black_moves)
        score += mobility_value

        wking_sq = self.board.king(chess.WHITE)
        bking_sq = self.board.king(chess.BLACK)
        if wking_sq is not None:
            attackers_on_wking = len(self.board.attackers(chess.BLACK, wking_sq))
            if attackers_on_wking > 0:
            
                score -= 0.5 * attackers_on_wking
        if bking_sq is not None:
            attackers_on_bking = len(self.board.attackers(chess.WHITE, bking_sq))
            if attackers_on_bking > 0:
              
                score += 0.5 * attackers_on_bking

        for sq, piece in self.board.piece_map().items():
            if piece.piece_type == chess.PAWN:
                rank = chess.square_rank(sq)  
                if piece.color == chess.WHITE:
                
                    score += 0.05 * rank
                else:
                    score -= 0.05 * (7 - rank)


        white_bishops = sum(1 for p in self.board.piece_map().values() if p.piece_type == chess.BISHOP and p.color == chess.WHITE)
        black_bishops = sum(1 for p in self.board.piece_map().values() if p.piece_type == chess.BISHOP and p.color == chess.BLACK)
        if white_bishops >= 2:
            score += 0.25
        if black_bishops >= 2:
            score -= 0.25

        return score
