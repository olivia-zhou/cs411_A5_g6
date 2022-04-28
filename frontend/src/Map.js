import {
    Box,
    Button,
    ButtonGroup,
    Flex,
    HStack,
    IconButton,
    Input,
    SkeletonText,
    Text,
} from '@chakra-ui/react'
import { FaLocationArrow, FaTimes } from 'react-icons/fa'

import {
    useJsApiLoader,
    GoogleMap,
    Autocomplete,
    DirectionsRenderer,
} from '@react-google-maps/api'
import React, { useRef, useState } from 'react'

const center = { lat: 42.3497644, lng: -71.1041491}

function Map() {
    const { isLoaded } = useJsApiLoader({
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries: ['places']
    })

    const [map, setMap] = useState(/** @type google.maps.Map */ (null))
    const [directionsResponse, setDirectionsResponse] = useState(null)
    const [distance, setDistance] = useState('')
    const [duration, setDuration] = useState('')
    const [latlng, setLatLng] = useState('')
    
    const originRef = useRef()
    const destiantionRef = useRef()

    const panTo = React.useCallback(({ lat, lng }) => {
        map.panTo({ lat, lng });
        map.setZoom(14);
    }, []);

    if (!isLoaded) {
        return <SkeletonText />
    }

    async function calculateRoute() {
        if (originRef.current.value === '' || destiantionRef.current.value === '') {
            return
        }
        // eslint-disable-next-line no-undef
        const directionsService = new google.maps.DirectionsService()
        const results = await directionsService.route({
            origin: originRef.current.value,
            destination: destiantionRef.current.value,
            // eslint-disable-next-line no-undef
            travelMode: google.maps.TravelMode.WALKING,
        })
        setDirectionsResponse(results)
        setDistance(results.routes[0].legs[0].distance.text)
        setDuration(results.routes[0].legs[0].duration.text)
        setLatLng(results.routes[0].legs[0].start_location)
    }

    function clearRoute() {
        setDirectionsResponse(null)
        setDistance('')
        setDuration('')
        setLatLng(center)
        originRef.current.value = ''
        destiantionRef.current.value = ''
        panTo(center)
    }
    
    function locate(){
        navigator.geolocation.getCurrentPosition(
            (position) => {
                map.panTo({
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                })
            },
            () => null
        )
    }
    
    return (
        <Flex
            position='relative'
            flexDirection='column'
            alignItems='center'
            h='80vh'
            w='80vw'
        >
            <Box position='absolute' left={0} top={0} h='100%' w='100%'>
                <GoogleMap
                    center={center}
                    zoom={13}
                    mapContainerStyle={{ width: '100%', height: '100%' }}
                    options={{
                        zoomControl: false,
                        streetViewControl: false,
                        mapTypeControl: false,
                        fullscreenControl: false,
                    }}
                    onLoad={map => setMap(map)}
                    >
                    {directionsResponse && (
                        <DirectionsRenderer directions={directionsResponse} />
                    )}

                </GoogleMap>
            </Box>
            <Box
                p={4}
                borderRadius='lg'
                m={4}
                bgColor='black'
                shadow='base'
                minW='container.md'
                zIndex='1'
            >
                <HStack spacing={2} justifyContent='space-between'>
                    <Box flexGrow={1}>
                        <Autocomplete>
                            <Input type='text' placeholder='Origin' ref={originRef} />
                        </Autocomplete>
                    </Box>
                    <Box flexGrow={1}>
                        <Autocomplete>
                            <Input
                                type='text'
                                placeholder='Destination'
                                ref={destiantionRef}
                            />
                        </Autocomplete>
                    </Box>

                    <ButtonGroup>
                        <Button colorScheme='pink' type='submit' onClick={calculateRoute}>
                            Calculate Route
                        </Button>
                        <IconButton
                            aria-label='center back'
                            icon={<FaTimes />}
                            onClick={clearRoute}
                        />
                    </ButtonGroup>
                </HStack>
                <HStack spacing={4} mt={3} justifyContent='space-between'>
                    <Text>Distance: {distance} </Text>
                    <Text>Duration: {duration} </Text>
                    <IconButton
                        aria-label='autoLocate'
                        icon={<FaLocationArrow />}
                        isRound
                        onClick={locate}
                    />
                </HStack>
            </Box>
        </Flex>
    )
}

export default Map