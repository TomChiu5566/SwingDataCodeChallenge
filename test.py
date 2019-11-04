from swingClass import swing

def main():
	latestSwing = swing('./latestSwing.csv')
	#latestSwing.print()
	
	# Basic tests of searchContinuityAboveValue
	print('Tests of searchContinuityAboveValue:')
	print('Test index 0 1275:', latestSwing.searchContinuityAboveValue('ax', 0, 1275, -1.2, 5))
	print('Test index 0 3:', latestSwing.searchContinuityAboveValue('ax', 0, 3, -1.2, 5))
	print('Test index 1271 1275:', latestSwing.searchContinuityAboveValue('ax', 1271, 1275, -0.2, 5))
	print('Test index 1272 1275:', latestSwing.searchContinuityAboveValue('ax', 1272, 1275, -0.2, 5))
	print('Test threshold 0:', latestSwing.searchContinuityAboveValue('ax', 0, 1275, 0, 5))
	print('Test threshold 1:', latestSwing.searchContinuityAboveValue('ax', 0, 1275, 1.0, 5))

	# Basic tests of backSearchContinuityWithinRange
	print('\nTests of backSearchContinuityWithinRange:')
	print('Test index 1275 0:', latestSwing.backSearchContinuityWithinRange('ax', 1275, 0, 0, 1, 5))
	print('Test index 1264 1261:', latestSwing.backSearchContinuityWithinRange('ax', 1264, 1261, 0, 1, 5))
	print('Test index 5 0:', latestSwing.backSearchContinuityWithinRange('ax', 5, 0, -1.2, -0.9, 5))
	print('Test index 3 0:', latestSwing.backSearchContinuityWithinRange('ax', 3, 0, -1.2, -0.9, 5))

	# Basic tests of searchContinuityAboveValueTwoSignals
	print('\nTests of searchContinuityAboveValueTwoSignals:')
	print('Test threshold 1 1:', latestSwing.searchContinuityAboveValueTwoSignals('ax', 'ay', 0, 1275, 1, 1, 5))
	print('Test index 35 45:', latestSwing.searchContinuityAboveValueTwoSignals('ax', 'ay', 35, 45, 1, 1, 5))

	# Basic tests of searchMultiContinuityWithinRange
	print('\nTests of searchMultiContinuityWithinRange:')
	print('Test index 0 1275:', latestSwing.searchMultiContinuityWithinRange('ax', 0, 1275, 0, 1, 5))
	


if __name__ == "__main__":
	main()
