def decorateurCheckIndex(f) :
        def checkIndex(self, i, j, *arg) :
            if i < 0 or i >= self.dim or j < 0 or j >= self.dim :
                print(f"[ERROR] Tiles to modify out of range [{i}],[{j}] >= {self.dim}")
                return None
            return f(self,i,j,*arg)
        return checkIndex