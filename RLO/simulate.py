
class Simulate:
	def __init__(self, Game:object, adversary, n_iteration = 1000) -> None:
		self.game = Game
		self.adversary = adversary
		self.n_iteration = n_iteration

	def simulate_INDCPA(self, verbose = False, n_iteration = 1000):
		self.n_iteration = n_iteration
		left_success = 0
		left_game = 0
		right_success = 0
		right_game = 0
		success = 0

		for _ in range(self.n_iteration):
			self.game._initialize()
			adv_output = self.adversary(self.game)
			if self.game.finalize(adv_output) == True:
				success += 1

			if self.game._b == '0':
				left_game += 1 
				if adv_output == True: 
					left_success += 1

			if self.game._b == '1':
				right_game += 1 
				if adv_output == True: 
					right_success += 1
				
		if verbose == True:
			print(f"Pr[Left => 1] = {left_success} / {left_game} = {left_success/left_game}\n")
			print(f"Pr[Right => 1] = {right_success} / {right_game} = {right_success/right_game}\n")
		print(f"Adv(A) = {right_success/right_game - left_success/left_game}" )


	def simulate_PRF(self, verbose = False, n_iteration = 1000):
		self.n_iteration = n_iteration
		real_success = 0
		real_game = 0
		random_success = 0
		random_game = 0
		success = 0

		for _ in range(self.n_iteration):
			self.game._initialize()
			adv_output = self.adversary(self.game)
			if self.game.finalize(adv_output) == True:
				success += 1

			if self.game._b == '0':
				real_game += 1 
				if adv_output == True: 
					real_success += 1

			if self.game._b == '1':
				random_game += 1 
				if adv_output == True: 
					random_success += 1
				
		if verbose == True:
			print(f"Pr[Real => 1] = {real_success} / {real_game} = {real_success/real_game}\n")
			print(f"Pr[Random => 1] = {random_success} / {random_game} = {random_success/random_game}\n")
		print(f"Adv(A) = {real_success/real_game - random_success/random_game}" )


	def simulate_cr(self, verbose = False, n_iteration = 1000):
		success = 0
		for _ in range(n_iteration):
			self.game._initialize()
			adv_output = self.adversary(self.game)
			if self.game.finalize(adv_output[0], adv_output[1]) == True:
				success += 1

		if verbose == True:
			print(f"Pr[CR_H => 1] = {success} / {n_iteration} = {success/n_iteration}\n")
		print(f"Adv(A) = {success/n_iteration}")


	def simulate_ufcma(self, verbose = False, n_iteration = 1000):
		success = 0
		for _ in range(n_iteration):
			self.game._initialize()
			adv_output = self.adversary(self.game)
			if self.game.finalize(adv_output[0], adv_output[1]) == True:
				success += 1
		if verbose == True:
			print(f"Pr[UFCMA_T => 1] = {success} / {n_iteration} = {success/n_iteration}\n")
		print(f"Adv(A) = {success/n_iteration}")


	def simulate_intctxt(self, verbose = False, n_iteration = 1000):
		success = 0
		for _ in range(n_iteration):
			self.game._initialize()
			adv_output = self.adversary(self.game)
			if self.game.finalize(adv_output) == True:
				success += 1
		if verbose == True:
			print(f"Pr[INTCTXT_AE => 1] = {success} / {n_iteration} = {success/n_iteration}\n")
		print(f"Adv(A) = {success/n_iteration}")


